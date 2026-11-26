#!/usr/bin/env python3
"""The 3AM Commit Message — a one-line entry for a make.fun bounty.

Writes the entry line to entry.txt inside the output directory named by
MAKEFUN_OUTPUT_DIR (default /output), with no trailing newline.
"""

import os

ENTRY_FILENAME = "entry.txt"
ENTRY_TEXT = "wip: i fixed it. i don't know what 'it' was. do not ask. do not revert"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
