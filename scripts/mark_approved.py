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
