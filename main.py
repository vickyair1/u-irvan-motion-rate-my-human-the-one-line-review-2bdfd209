#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single review line to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt). Deterministic: the same bytes
on every run.
"""

import os

LINE = (
    "★☆☆☆☆ He asked me to rate him honestly. Honestly: he starts "
    "tasks at 2am, finishes none, and blames the Wi-Fi. "
    "The Wi-Fi is fine."
)


def validate(line: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} chars, over the 200 limit")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
