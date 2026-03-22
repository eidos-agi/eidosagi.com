import type { APIRoute } from 'astro';
import { appendFileSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const FEEDBACK_FILE = join(process.cwd(), 'feedback.jsonl');
const MAX_BODY_SIZE = 10_000; // 10KB
const MAX_UA_LENGTH = 256;

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  try {
    const raw = await request.text();
    if (raw.length > MAX_BODY_SIZE) {
      return new Response(JSON.stringify({ error: 'Payload too large' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const body = JSON.parse(raw);
    if (!body || typeof body !== 'object') {
      return new Response(JSON.stringify({ error: 'Invalid body' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const ua = (request.headers.get('user-agent') || '').slice(0, MAX_UA_LENGTH);

    const entry = {
      ...body,
      received: new Date().toISOString(),
      ua,
    };

    appendFileSync(FEEDBACK_FILE, JSON.stringify(entry) + '\n', 'utf-8');

    return new Response(JSON.stringify({ ok: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch {
    return new Response(JSON.stringify({ error: 'Bad request' }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};

export const GET: APIRoute = async () => {
  if (!existsSync(FEEDBACK_FILE)) {
    return new Response(JSON.stringify([]), {
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const lines = readFileSync(FEEDBACK_FILE, 'utf-8')
    .split('\n')
    .filter(Boolean);

  const entries = [];
  for (const line of lines) {
    try {
      entries.push(JSON.parse(line));
    } catch {
      // Skip malformed lines
    }
  }

  return new Response(JSON.stringify(entries), {
    headers: { 'Content-Type': 'application/json' },
  });
};
