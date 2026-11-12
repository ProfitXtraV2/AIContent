// The dashboard and GitHub (social posts, product spec E, F6, F7, D). The page holds no key: it reads
// what a public repository shows anyone (the API without a token, raw files) and everything a person
// does goes through GitHub pages they confirm with their own login: a PR to merge or close, a file to
// edit, or a new issue the dashboard fills in for them ("social: …", done by social-intake.yml).
// `?repo=owner/name` is honoured only on localhost (testing), never on the published page; localhost
// remembers it, so the address without it stays on the same repository.
const SocialGitHub = (() => {
  const API = 'https://api.github.com';
  const LOCAL = ['localhost', '127.0.0.1'].includes(location.hostname);
  const REPO_KEY = 'px-social-repo';
  const valid = r => !!r && /^[\w.-]+\/[\w.-]+$/.test(r);
  let asked = new URLSearchParams(location.search).get('repo');
  if (LOCAL && valid(asked)) { try { localStorage.setItem(REPO_KEY, asked); } catch (e) { /* not kept */ } }
  else if (LOCAL) { try { asked = localStorage.getItem(REPO_KEY); } catch (e) { asked = null; } }
  const REPO = LOCAL && valid(asked) ? asked : 'ProfitXtraV2/AIContent';
  const WEB = `https://github.com/${REPO}`;
  const MAX_URL = 7500;                          // longer new-issue links go through the clipboard

  function b64decode(b64) {
    const bin = atob(String(b64 || '').replace(/\n/g, ''));
    return new TextDecoder('utf-8').decode(Uint8Array.from(bin, c => c.charCodeAt(0)));
  }
  const encPath = p => String(p).split('/').map(encodeURIComponent).join('/');

  const MESSAGES = { 403: 'GitHub limits how often a page may read it: try again in a while',
                     404: 'not found (a private repository shows nothing without signing in to GitHub)' };

  async function call(path, accept) {
    const resp = await fetch(API + path, { headers: { Accept: accept || 'application/vnd.github+json' }, cache: 'no-store' });
    if (!resp.ok) {
      const err = new Error(`${MESSAGES[resp.status] || 'GitHub error'} (HTTP ${resp.status})`);
      err.status = resp.status;
      throw err;
    }
    return accept === 'application/vnd.github.raw' ? resp.blob() : resp.json();
  }
  const repo = p => `/repos/${REPO}${p}`;

  // reading (a public repository)
  async function getFile(path, ref) {
    const j = await call(repo(`/contents/${encPath(path)}?ref=${encodeURIComponent(ref || 'main')}`));
    return { text: b64decode(j.content), sha: j.sha };
  }
  const imageUrl = async (path, ref) => `https://raw.githubusercontent.com/${REPO}/${encodeURIComponent(ref)}/${encPath(path)}`;
  const pulls = state => call(repo(`/pulls?state=${state || 'open'}&per_page=100`));
  const pull = n => call(repo(`/pulls/${+n}`));
  const combinedStatus = sha => call(repo(`/commits/${encodeURIComponent(sha)}/status`));
  const comments = n => call(repo(`/issues/${+n}/comments?per_page=100`));

  // the GitHub pages a person acts on
  const prUrl = n => `${WEB}/pull/${+n}`;
  const editUrl = (branch, path) => `${WEB}/edit/${encPath(branch)}/${encPath(path)}`;
  const issuesUrl = query => `${WEB}/issues?q=${encodeURIComponent(query)}`;
  const pullsUrl = query => `${WEB}/pulls?q=${encodeURIComponent(query)}`;
  const newIssueUrl = (title, body) => `${WEB}/issues/new?title=${encodeURIComponent(title)}&body=${encodeURIComponent(body || '')}`;

  // a new issue in a new tab; a body too long for a link goes to the clipboard, to paste there
  async function openIssue(title, body) {
    let url = newIssueUrl(title, body), copied = false;
    if (url.length > MAX_URL) {
      try { await navigator.clipboard.writeText(body); copied = true; } catch (e) { copied = false; }
      url = newIssueUrl(title, copied ? '(Ctrl+V)' : body.slice(0, 2000));
    }
    window.open(url, '_blank', 'noopener');
    return { url, copied };
  }

  return { REPO, LOCAL, WEB, getFile, imageUrl, pulls, pull, combinedStatus, comments, prUrl, editUrl, issuesUrl,
           pullsUrl, newIssueUrl, openIssue, b64decode };
})();
