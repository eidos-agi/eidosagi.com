import type { APIRoute } from 'astro';
import { appendFileSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const FEEDBACK_FILE = join(process.cwd(), 'feedback.jsonl');

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  const body = await request.json();

  const entry = {
    ...body,
    received: new Date().toISOString(),
    ua: request.headers.get('user-agent') || '',
  };

  appendFileSync(FEEDBACK_FILE, JSON.stringify(entry) + '\n', 'utf-8');

  return new Response(JSON.stringify({ ok: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  });
};

export const GET: APIRoute = async () => {
  if (!existsSync(FEEDBACK_FILE)) {
    return new Response(JSON.stringify([]), {
      headers: { 'Content-Type': 'application/json' },
    });
  }

  const lines = readFileSync(FEEDBACK_FILE, 'utf-8')
    .split('\n')
    .filter(Boolean)
    .map(line => JSON.parse(line));

  return new Response(JSON.stringify(lines), {
    headers: { 'Content-Type': 'application/json' },
  });
};
