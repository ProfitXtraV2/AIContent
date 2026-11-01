"""Markdown tables in the boards (settings, requests, packs), parsed by header name.

The same convention as scripts/mark_approved.py: a table is a header row, a separator row
and data rows, every row written as `| c1 | c2 | ... |`. Cells may not contain a bare `|`.
"""
import re


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_sep(cells):
    return all(set(c) <= set("-: ") for c in cells if c) and any(cells)


def tables(md_text):
    """Every table in the text, in order: [{header: [..], rows: [{col: value}], start, end}]
    with start/end line indexes (end exclusive) so callers can rewrite a table in place."""
    lines = md_text.splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and i + 1 < len(lines) and lines[i + 1].strip().startswith("|") \
                and _is_sep(_cells(lines[i + 1])):
            header = [c.lower() for c in _cells(line)]
            j, rows = i + 2, []
            while j < len(lines) and lines[j].strip().startswith("|"):
                cells = _cells(lines[j])
                cells += [""] * (len(header) - len(cells))
                rows.append(dict(zip(header, cells[:len(header)])))
                j += 1
            out.append({"header": header, "rows": rows, "start": i, "end": j})
            i = j
        else:
            i += 1
    return out


def find(md_text, *required_columns):
    """The first table whose header holds all the given columns, or None."""
    want = [c.lower() for c in required_columns]
    for t in tables(md_text):
        if all(c in t["header"] for c in want):
            return t
    return None


def render_row(header, row):
    return "| " + " | ".join(clean(row.get(h, "")) for h in header) + " |"


def render(header, rows):
    """A whole table: header, separator and rows."""
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    lines += [render_row(header, r) for r in rows]
    return "\n".join(lines)


def replace(md_text, table, rows):
    """The text with `table` (as returned by tables()/find()) holding `rows` instead."""
    lines = md_text.splitlines()
    new = render(table["header"], rows).splitlines()
    out = lines[:table["start"]] + new + lines[table["end"]:]
    return "\n".join(out) + ("\n" if md_text.endswith("\n") else "")


def with_columns(table, columns):
    """The table with any of `columns` it lacks put in at their place (a table written before
    those columns existed); its rows read the new cells as empty (docs/social-md.js withColumns)."""
    header = list(table["header"])
    for i, c in enumerate(columns):
        if c in header:
            continue
        before = next((p for p in reversed(columns[:i]) if p in header), None)
        header.insert(header.index(before) + 1 if before else 0, c)
    return dict(table, header=header)


def clean(value):
    """A value safe in a cell: one line, no bare pipe."""
    return re.sub(r"\s+", " ", str(value if value is not None else "")).replace("|", "/").strip()


def split_list(value):
    """'a, b, c' → ['a', 'b', 'c'] (empty items dropped)."""
    return [v.strip() for v in str(value or "").split(",") if v.strip()]
