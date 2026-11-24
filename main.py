"""Autocorrect fail writer for the make.fun bounty.

Running this module writes a single one-line autocorrect fail to
/output/entry.txt. The text is fixed: the program holds no randomness,
makes no network calls and creates no other files.
"""

import os

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

FAIL_LINE = (
    "I texted my boss 'I love you' instead of 'I'll see you'. "
    "Autocorrect has filed for my resignation and my promotion."
)


def publish_fail() -> str:
    """Save the autocorrect fail line and hand it back to the caller."""
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FAIL_LINE)
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        stored = handle.read()
    if stored != FAIL_LINE:
        raise ValueError("entry.txt does not match the intended line")
    return stored


if __name__ == "__main__":
    publish_fail()
