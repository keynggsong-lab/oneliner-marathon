"""One-Liner Marathon — entry program.

Writes one line, one-line joke, to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only, no network, fully deterministic: the same bytes every run.
"""

import os
from pathlib import Path

LINE = "My AI assistant is so confident it once corrected the dictionary, and the dictionary apologized."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def main() -> None:
    # Gate mirror: the sealed scorer requires UTF-8 text of 1-280 chars,
    # not only white space. Refuse to write an invalid entry.
    text = LINE
    assert 1 <= len(text) <= 280, "line must be 1-280 characters"
    assert text.strip(), "line must not be only white space"
    text.encode("utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
