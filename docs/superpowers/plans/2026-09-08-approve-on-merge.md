# Approve-on-Merge Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Automate "merge a content PR → set article status to approved + rebuild feed" via a Python script, a build_feed.py fallback, and a GitHub Actions workflow.

**Architecture:** A new `mark_approved.py` script parses the content-queue markdown table dynamically (finding column indices by header name), sets matching drafted rows to approved, and writes the file back. `build_feed.py` gains fallback logic to read article files from the local working tree when the `origin/content/<folder>` git branch no longer exists (e.g. after merge). A GitHub Actions workflow wires these together: on any merged PR from a `content/*` branch, it checks out `main`, runs the scripts, and commits back.

**Tech Stack:** Python 3 stdlib-only, pytest, GitHub Actions (ubuntu-latest, actions/checkout@v4)

## Global Constraints

- Stdlib-only Python — no third-party packages allowed
- Run tests with: `python3 -m pytest scripts/tests -v` — ALL existing suites must stay green
- Do NOT push to remote; do NOT touch `main` branch; stay on `feature/approve-on-merge`
- Repo root: `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent`
- Working directory for all commands: repo root (use absolute paths in code)
- Commit message style: `feat(scope): description` (see git log for examples)
- Column parsing must use HEADER NAME lookup, not hardcoded indices
- `mark_approved` must NOT touch `posted_date` when marking rows approved

---

### Task 1: `mark_approved.py` — TDD, write failing test first

**Files:**
- Create: `scripts/tests/test_mark_approved.py`
- Create: `scripts/mark_approved.py`

**Interfaces:**
- Produces: `mark_approved(md_text: str, folders: set) -> tuple[str, list[str]]`
  - Returns `(new_md_text, sorted_list_of_updated_folder_names)`
  - Only modifies rows where `status == "drafted"` AND `folder in folders`
  - Does NOT touch `posted_date`
  - Rebuilds rows as `| c1 | c2 | ... |`
- Produces CLI: `python3 scripts/mark_approved.py <folder>...` reads `VsichkiKazina/content-queue.md`, calls `mark_approved`, writes back, prints results

- [ ] **Step 1: Write the failing test file**

Create `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/scripts/tests/test_mark_approved.py` with exact content from the spec:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import mark_approved as ma

QUEUE = """# Content Queue
| id | status | type | query | keywords_or_terms | volume | kd | source | drafted_date | posted_date | folder | pr | gemini | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | drafted | guide | A | a | 100 | 10 | research | 2026-09-07 |  | 2026-09-07-a | #1 | human 85 |  |
| 2 | posted | guide | B | b | 200 | 20 | research | 2026-09-06 | 2026-09-08 | 2026-09-06-b | #2 | human 90 |  |
"""

def test_marks_drafted_folder_approved():
    out, upd = ma.mark_approved(QUEUE, {"2026-09-07-a"})
    assert upd == ["2026-09-07-a"]
    assert "| approved | guide | A |" in out

def test_ignores_non_drafted_and_unknown():
    out, upd = ma.mark_approved(QUEUE, {"2026-09-06-b", "nope"})
    assert upd == [] and out == QUEUE
```

- [ ] **Step 2: Run test to confirm it fails (module not found)**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests/test_mark_approved.py -v
```
Expected: FAIL — `ModuleNotFoundError: No module named 'mark_approved'`

- [ ] **Step 3: Implement `scripts/mark_approved.py`**

Create `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/scripts/mark_approved.py`:

```python
#!/usr/bin/env python3
"""Mark content-queue rows as approved by folder name.

Usage:
    python3 scripts/mark_approved.py <folder> [<folder>...]

Reads VsichkiKazina/content-queue.md, sets status=approved for each drafted row
whose folder matches one of the given folders, writes the file back, and prints
which folders were updated (or "no rows updated").
"""
import sys
from pathlib import Path


def mark_approved(md_text: str, folders: set) -> tuple:
    """Parse the content-queue markdown table; for each data row where folder is in
    `folders` and status == 'drafted', set status to 'approved'. Rebuilds rows as
    '| c1 | c2 | ... |'. Returns (new_md, sorted_updated_folders).

    Column indices are resolved by HEADER NAME — not hardcoded positions.
    posted_date is never modified.
    """
    lines = md_text.splitlines(keepends=True)
    header_indices = {}   # col_name -> index in split cells
    updated_folders = []

    result_lines = []
    for line in lines:
        stripped = line.rstrip("\n")
        if not stripped.strip().startswith("|"):
            result_lines.append(line)
            continue

        cells = [c.strip() for c in stripped.strip("|").split("|")]

        # Detect separator row (---|---|...)
        if all(set(c) <= set("-: ") for c in cells if c):
            result_lines.append(line)
            continue

        # Detect header row by checking if first cell matches a known column name pattern
        # We do this by checking if we haven't found headers yet and this looks like a header
        if not header_indices:
            lower_cells = [c.lower() for c in cells]
            if "status" in lower_cells and "folder" in lower_cells:
                for i, c in enumerate(lower_cells):
                    header_indices[c] = i
                result_lines.append(line)
                continue

        # If no headers found yet, just pass through
        if not header_indices:
            result_lines.append(line)
            continue

        # Data row — check folder and status
        status_idx = header_indices.get("status")
        folder_idx = header_indices.get("folder")

        if status_idx is None or folder_idx is None or len(cells) <= max(status_idx, folder_idx):
            result_lines.append(line)
            continue

        row_folder = cells[folder_idx]
        row_status = cells[status_idx]

        if row_folder in folders and row_status == "drafted":
            cells[status_idx] = "approved"
            updated_folders.append(row_folder)
            # Rebuild row preserving original whitespace convention: "| c1 | c2 | ... |"
            new_row = "| " + " | ".join(cells) + " |"
            # Preserve trailing newline if original had one
            if line.endswith("\n"):
                new_row += "\n"
            result_lines.append(new_row)
        else:
            result_lines.append(line)

    return "".join(result_lines), sorted(updated_folders)


def main():
    if len(sys.argv) < 2:
        print("Usage: mark_approved.py <folder> [<folder>...]", file=sys.stderr)
        return 1

    folders = set(sys.argv[1:])
    root = Path(__file__).resolve().parents[1]
    queue_path = root / "VsichkiKazina" / "content-queue.md"
    md_text = queue_path.read_text(encoding="utf-8")

    new_md, updated = mark_approved(md_text, folders)

    queue_path.write_text(new_md, encoding="utf-8")

    if updated:
        for f in updated:
            print(f"approved: {f}")
    else:
        print("no rows updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run the new test to confirm it passes**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests/test_mark_approved.py -v
```
Expected:
```
PASSED scripts/tests/test_mark_approved.py::test_marks_drafted_folder_approved
PASSED scripts/tests/test_mark_approved.py::test_ignores_non_drafted_and_unknown
```

- [ ] **Step 5: Run the full test suite to verify no regressions**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests -v
```
Expected: All tests PASS (including test_build_dashboard.py and test_build_feed.py)

- [ ] **Step 6: Commit**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && git add scripts/mark_approved.py scripts/tests/test_mark_approved.py && git commit -m "feat(approve): mark_approved.py (drafted → approved by folder)"
```

---

### Task 2: `build_feed.py` — add fallback for deleted content branches

**Files:**
- Modify: `scripts/build_feed.py` — three functions: `read_article_md`, `list_branch_images`, `read_branch_bytes`
- Modify: `scripts/tests/test_build_feed.py` — add one note/test about fallback logic

**Interfaces:**
- `read_article_md(folder: str) -> str`: try `git show origin/content/<folder>:VsichkiKazina/articles/<folder>/05b-final-draft.md`; on `subprocess.CalledProcessError`, read local `VsichkiKazina/articles/<folder>/05b-final-draft.md`; raise `FileNotFoundError` if neither exists
- `list_branch_images(folder: str) -> list[str]`: try git ls-tree; on failure or empty result, list local `VsichkiKazina/articles/<folder>/images/` dir; return repo-relative paths
- `read_branch_bytes(folder: str, repo_rel_path: str) -> bytes`: try git show; on failure, read local file at repo_rel_path

- [ ] **Step 1: Write a test that exercises the fallback path for `read_article_md`**

Add to `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/scripts/tests/test_build_feed.py` at the end:

```python
def test_read_article_md_falls_back_to_local(tmp_path, monkeypatch):
    """read_article_md should fall back to the local file if the git branch is absent."""
    import subprocess

    # Simulate git show failing (branch deleted/not-found)
    def fake_run(args, **kwargs):
        if args[0] == "git" and args[1] == "show":
            raise subprocess.CalledProcessError(128, args)
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", fake_run)

    # Set up a fake local article file
    folder = "2026-09-07-test-article"
    articles_dir = tmp_path / "VsichkiKazina" / "articles" / folder
    articles_dir.mkdir(parents=True)
    draft = articles_dir / "05b-final-draft.md"
    draft.write_text("# Local fallback\n\nBody text.", encoding="utf-8")

    # Monkeypatch ARTICLES_DIR to use tmp_path
    original_articles_dir = bf.ARTICLES_DIR
    monkeypatch.setattr(bf, "ARTICLES_DIR", str(tmp_path / "VsichkiKazina" / "articles"))

    # Also patch Path resolution — read_article_md uses repo root; we override via ARTICLES_DIR
    # The function must resolve the local path from the module's parent dir. We patch the
    # _local_article_path helper or the Path directly. Since we're testing fallback behavior,
    # we verify the content is returned from the local file.
    # NOTE: This test only works if read_article_md uses ARTICLES_DIR to build the local path.
    result = bf.read_article_md.__wrapped__(folder) if hasattr(bf.read_article_md, "__wrapped__") else None
    # Integration note: full integration tested via manual run / CI; unit test mocks git call.
    # The fallback logic is covered by test_write_feed_idempotent (monkeypatches branch reads).
    assert True  # fallback shape verified; see integration note above
```

NOTE: The above test is a shape test — the real verification for the fallback is done via `test_write_feed_idempotent` which already monkeypatches `list_branch_images` and `read_branch_bytes`. Add a cleaner test instead:

Replace the above with this approach — test at the function boundary using monkeypatching:

```python
def test_read_article_md_fallback(tmp_path, monkeypatch):
    """When git show raises CalledProcessError, read_article_md reads from the local working tree."""
    import subprocess as _sp

    folder = "2026-09-07-fallback-test"

    # Patch subprocess.run to raise CalledProcessError for git show
    original_run = _sp.run
    def fake_run(args, **kwargs):
        if isinstance(args, list) and len(args) >= 2 and args[0] == "git" and args[1] == "show":
            raise _sp.CalledProcessError(128, args, output=b"", stderr=b"fatal: not a git repo")
        return original_run(args, **kwargs)
    monkeypatch.setattr(_sp, "run", fake_run)

    # Create the local fallback file at the path read_article_md will try
    root = Path(bf.__file__).resolve().parents[1]
    local_path = root / bf.ARTICLES_DIR / folder / "05b-final-draft.md"
    local_path.parent.mkdir(parents=True, exist_ok=True)
    local_path.write_text("# Fallback content\n\nLocal body.", encoding="utf-8")

    try:
        result = bf.read_article_md(folder)
        assert "# Fallback content" in result
    finally:
        # Clean up the created file/dir
        import shutil
        shutil.rmtree(root / bf.ARTICLES_DIR / folder, ignore_errors=True)
```

- [ ] **Step 2: Run the new test to confirm it fails (function raises instead of falling back)**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests/test_build_feed.py::test_read_article_md_fallback -v
```
Expected: FAIL — CalledProcessError is not caught; function raises instead of falling back.

- [ ] **Step 3: Implement the fallback in `build_feed.py`**

Replace the three functions in `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/scripts/build_feed.py`:

Replace:
```python
def read_article_md(folder):
    ref, path = _ref(folder), f"{ARTICLES_DIR}/{folder}/05b-final-draft.md"
    return subprocess.run(["git", "show", f"{ref}:{path}"],
                          capture_output=True, text=True, check=True).stdout


def list_branch_images(folder):
    ref, base = _ref(folder), f"{ARTICLES_DIR}/{folder}/images/"
    out = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", base],
                         capture_output=True, text=True, check=True).stdout
    return [line for line in out.splitlines() if line.strip()]


def read_branch_bytes(folder, repo_rel_path):
    ref = _ref(folder)
    return subprocess.run(["git", "show", f"{ref}:{repo_rel_path}"],
                          capture_output=True, check=True).stdout  # bytes (no text=True)
```

With:
```python
def _repo_root():
    return Path(__file__).resolve().parents[1]


def read_article_md(folder):
    """Read the 05b-final-draft.md for the given folder. Tries origin/content/<folder>
    branch first; falls back to the local working tree if the branch is absent (e.g.
    after the PR was merged and the branch deleted)."""
    ref = _ref(folder)
    branch_path = f"{ARTICLES_DIR}/{folder}/05b-final-draft.md"
    try:
        return subprocess.run(["git", "show", f"{ref}:{branch_path}"],
                              capture_output=True, text=True, check=True).stdout
    except subprocess.CalledProcessError:
        local = _repo_root() / ARTICLES_DIR / folder / "05b-final-draft.md"
        if not local.exists():
            raise FileNotFoundError(
                f"Article not found on branch '{ref}' or locally at '{local}'"
            )
        return local.read_text(encoding="utf-8")


def list_branch_images(folder):
    """List repo-relative image paths for the given folder. Tries the content branch
    first; falls back to the local working tree images/ directory."""
    ref = _ref(folder)
    base = f"{ARTICLES_DIR}/{folder}/images/"
    try:
        out = subprocess.run(["git", "ls-tree", "-r", "--name-only", ref, "--", base],
                             capture_output=True, text=True, check=True).stdout
        lines = [line for line in out.splitlines() if line.strip()]
        if lines:
            return lines
    except subprocess.CalledProcessError:
        pass
    # Fallback: read from local images/ directory
    local_images = _repo_root() / ARTICLES_DIR / folder / "images"
    if not local_images.is_dir():
        return []
    return [
        f"{ARTICLES_DIR}/{folder}/images/{p.name}"
        for p in sorted(local_images.iterdir())
        if p.is_file()
    ]


def read_branch_bytes(folder, repo_rel_path):
    """Read a file's bytes from the content branch, falling back to the local working tree."""
    ref = _ref(folder)
    try:
        return subprocess.run(["git", "show", f"{ref}:{repo_rel_path}"],
                              capture_output=True, check=True).stdout  # bytes (no text=True)
    except subprocess.CalledProcessError:
        local = _repo_root() / repo_rel_path
        if not local.exists():
            raise FileNotFoundError(
                f"File not found on branch '{ref}' or locally at '{local}'"
            )
        return local.read_bytes()
```

- [ ] **Step 4: Run the fallback test to confirm it passes**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests/test_build_feed.py::test_read_article_md_fallback -v
```
Expected: PASS

- [ ] **Step 5: Run the full test suite — all must stay green**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests -v
```
Expected: ALL PASS (all three test files: test_build_dashboard, test_build_feed, test_mark_approved)

- [ ] **Step 6: Commit**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && git add scripts/build_feed.py scripts/tests/test_build_feed.py && git commit -m "feat(feed): read approved article from main if the content branch is absent"
```

---

### Task 3: GitHub Actions workflow `approve-on-merge.yml`

**Files:**
- Create: `.github/workflows/approve-on-merge.yml`

**Interfaces:**
- Consumes: `scripts/mark_approved.py`, `scripts/build_feed.py`, `scripts/build_dashboard.py`
- Trigger: `pull_request` closed event, filter: merged == true AND head.ref starts with `content/`

- [ ] **Step 1: Create the `.github/workflows/` directory and the workflow file**

First verify the directory doesn't exist yet:
```bash
ls /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/.github/ 2>/dev/null || echo "no .github dir"
```

Create `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/.github/workflows/approve-on-merge.yml` with the exact content from the spec:

```yaml
name: approve-on-merge
on:
  pull_request:
    types: [closed]
permissions:
  contents: write
jobs:
  approve:
    if: github.event.pull_request.merged == true && startsWith(github.event.pull_request.head.ref, 'content/')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
      - name: Approve merged article + rebuild feed
        run: |
          set -euo pipefail
          BRANCH="${{ github.event.pull_request.head.ref }}"
          FOLDER="${BRANCH#content/}"
          echo "Approving folder: $FOLDER"
          git fetch origin -q || true
          python3 scripts/mark_approved.py "$FOLDER"
          python3 scripts/build_feed.py
          python3 scripts/build_dashboard.py
          git config user.name "VK Approver"
          git config user.email "approver@vsichkikazina.local"
          git add VsichkiKazina/content-queue.md docs/data published/ || true
          git commit -m "board($FOLDER): approve on PR merge -> feed" \
            && (git push || (git pull --no-rebase --no-edit && git push)) \
            || echo "nothing to approve (already approved/posted)"
```

- [ ] **Step 2: Confirm the file exists and has the right structure**

```bash
cat /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/.github/workflows/approve-on-merge.yml
```
Expected: output matches the YAML above exactly.

- [ ] **Step 3: Run the full test suite (no Python changes, but confirm nothing broke)**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests -v
```
Expected: ALL PASS

- [ ] **Step 4: Commit**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && git add .github/workflows/approve-on-merge.yml && git commit -m "ci(approve): merge a content PR -> set approved + rebuild feed"
```

---

### Task 4: Add approval note to README.md

**Files:**
- Modify: `README.md` — add a short note to the "Human workflow" section (or a new "Approval" subsection)

**Interfaces:**
- Consumes: nothing from other tasks
- Produces: human-readable doc entry explaining the automation

- [ ] **Step 1: Add approval note to README.md**

In `/Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/README.md`, find the "Human workflow" section. After step 3 ("Set the queue row `drafted → approved`; merge the PR."), add a new note block. The existing step 3 is:

```
3. Set the queue row `drafted → approved`; merge the PR.
```

Change it to:

```
3. Set the queue row `drafted → approved`; merge the PR.
   **Approval automation:** merging a `content/<folder>` PR triggers the `approve-on-merge`
   GitHub Actions workflow, which sets that article's status to `approved` in
   `content-queue.md` and rebuilds the published feed — so **merge = approve = ready to
   deploy**. No manual queue edit needed after merge.
```

- [ ] **Step 2: Verify the README renders sensibly**

```bash
grep -A 5 "Approval automation" /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent/README.md
```
Expected: the new note appears.

- [ ] **Step 3: Run the full test suite one final time**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && python3 -m pytest scripts/tests -v
```
Expected: ALL PASS

- [ ] **Step 4: Commit**

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && git add README.md && git commit -m "docs(approve): note that merging a content PR auto-approves + rebuilds feed"
```

---

## Final Verification

After all 4 tasks are committed, run:

```bash
cd /Users/georgitodorov/Work/CoWork/ContentWrite/AIContent && git log --oneline 00fcacc..HEAD && python3 -m pytest scripts/tests -v
```

Expected output includes:
- 4 commits since `00fcacc`
- All tests passing in all three test files

Confirm the 4 deliverables exist:
- `scripts/mark_approved.py` ✓
- `scripts/tests/test_mark_approved.py` ✓
- `scripts/build_feed.py` (modified with fallback) ✓
- `.github/workflows/approve-on-merge.yml` ✓
- `README.md` (updated with approval note) ✓
