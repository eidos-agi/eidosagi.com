// Fetch GitHub stars and PyPI downloads at build time
// Returns 0 gracefully on failure — never blocks the build

export async function getGitHubStars(repo: string): Promise<number> {
  try {
    const res = await fetch(`https://api.github.com/repos/eidos-agi/${repo}`, {
      headers: { 'Accept': 'application/vnd.github.v3+json' },
    });
    if (!res.ok) return 0;
    const data = await res.json();
    return data.stargazers_count || 0;
  } catch {
    return 0;
  }
}

export async function getPyPIDownloads(pkg: string): Promise<number> {
  try {
    const res = await fetch(`https://pypistats.org/api/packages/${pkg}/recent`);
    if (!res.ok) return 0;
    const data = await res.json();
    return data?.data?.last_month || 0;
  } catch {
    return 0;
  }
}

export interface PyPIInfo {
  version: string;
  releaseDate: string;
}

export async function getPyPIInfo(pkg: string): Promise<PyPIInfo | null> {
  try {
    const res = await fetch(`https://pypi.org/pypi/${pkg}/json`);
    if (!res.ok) return null;
    const data = await res.json();
    const version = data?.info?.version || '';
    const releases = data?.releases?.[version];
    const releaseDate = releases?.[0]?.upload_time_iso_8601
      ? new Date(releases[0].upload_time_iso_8601).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })
      : '';
    return { version, releaseDate };
  } catch {
    return null;
  }
}
