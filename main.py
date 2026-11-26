"""Entry #181: Rejected Olympic Sports (make.fun).

Writes one funny one-line rejected Olympic sport to entry.txt in the
output directory named by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os

ENTRY = (
    "Synchronized spreadsheet diving: two accountants, one pivot table, "
    "zero survivors. Judges award points for the splash and deduct for "
    "the macros."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space. Refuse to run if the line ever drifts out.
    assert 1 <= len(ENTRY) <= 200, "entry outside the 1-200 character gate"
    assert ENTRY.strip() == ENTRY, "entry has leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the file holds exactly the 144-character line.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
