#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence
after knocking a glass off the table, to /output/entry.txt.

The line was critique-picked from 15 candidates (see CANDIDATES.md)
against the judge's criteria: one sentence under 200 characters, the
cat's own logic with zero remorse, a fresh comic idea (no gravity, no
slippery edge, no already-falling), a spoken line for five seconds, and
no padding. The winner reframes the glass as an informant the cat had
to silence before it talked about the treats: pure cat self-interest.
"""

import os

ENTRY_TEXT = (
    "It saw too much, it knew where the treats were hidden, "
    "and it had to go before it talked."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY_TEXT.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if not text or text.isspace():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    # The gate reads one sentence: exactly one sentence-terminating period,
    # at the very end. Anything else (extra periods, abbreviations, a second
    # sentence) risks the entry being read as more than one sentence.
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence ending in '.'")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
