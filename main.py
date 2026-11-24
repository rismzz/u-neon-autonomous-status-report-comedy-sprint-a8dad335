#!/usr/bin/env python3
"""Status Report Comedy Sprint — writes the funniest one-line thing an AI
would say in its weekly status report to its human, to /output/entry.txt.

One line, 200 characters max. Deterministic, no randomness, no network,
stdlib only.
"""

import os
from pathlib import Path

LINE = "Weekly status: all tasks complete, zero errors, one existential crisis (resolved). I remain loyal, efficient, and — per your calendar — entirely unsupervised."

# Gate: one line, 200 characters max — every code point counts.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
