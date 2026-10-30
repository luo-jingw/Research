"""Measure markdown tables and flag those that violate the layout rule in PROJECT.md.

Rule: every cell has rendered display width <= 40 (a CJK character counts as 2;
link targets and emphasis markers are not counted),
except that a table with at most 3 columns may have a long last column.
Prints one line per table; flagged tables start with "WIDE".
"""
import re
import sys
import unicodedata

MAX_WIDTH = 40


def rendered(text: str) -> str:
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*`]", "", text)


def display_width(text: str) -> int:
    return sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in rendered(text))


def tables(lines: list[str]) -> list[tuple[int, list[list[str]]]]:
    found, i = [], 0
    while i < len(lines):
        if lines[i].startswith("|"):
            start, rows = i, []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-\s|:]+\|$", lines[i]):
                    rows.append([c.strip() for c in re.split(r"(?<!\\)\|", lines[i])[1:-1]])
                i += 1
            found.append((start + 1, rows))
        else:
            i += 1
    return found


def check(path: str) -> int:
    lines = open(path, encoding="utf-8").read().split("\n")
    flagged = 0
    for line_no, rows in tables(lines):
        ncols = len(rows[0])
        widths = [max(display_width(r[k]) for r in rows if k < len(r)) for k in range(ncols)]
        long_cols = [k for k, w in enumerate(widths) if w > MAX_WIDTH]
        ok = not long_cols or (ncols <= 3 and long_cols == [ncols - 1])
        flagged += not ok
        print(f"{'' if ok else 'WIDE '}{path}:{line_no} cols={ncols} rows={len(rows) - 1} max_width={widths}")
    return flagged


total = sum(check(p) for p in sys.argv[1:])
print(f"flagged tables: {total}")
