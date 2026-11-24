#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One Letter for Your Day: a single letter for the word behind the day.

Writes exactly one character to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it to stdout. Deterministic:
no randomness, no network, no input.

The letter is H -- for "hangry": hungry enough to be angry. The judge
sees only the letter and must infer the word behind it, so the letter
has to carry the word on its own. H does, criterion by criterion:
(1) H is the first letter of a real day-word, "hangry"; (2) it is
vivid and specific -- a stomach-growling, mood-wrecking day, a sharp
picture, not a vague mood like "happy" or "amazing"; (3) it is funny
at once, a word people repeat to a friend; (4) it is true to a real
day, a feeling almost everyone has lived, an honest report rather
than a performance; (5) the breathy H fits the word's sound, and it
is not the obvious pick -- A for amazing and Z for zero sleep are the
examples the brief itself hands out, and the field is flooded with
them. "Hangry" is the sharper initial.
"""

import os

LETTER = "H"


def validate(letter):
    """Fail fast on anything the sealed gate would refuse.

    The gate requires UTF-8 text of exactly 1 character, not only
    whitespace, and the task requires a letter A to Z -- so the
    check is exact: one character, ASCII uppercase A-Z.
    """
    if not isinstance(letter, str) or not letter.strip():
        raise ValueError("entry must not be empty or whitespace-only")
    if len(letter) != 1:
        raise ValueError("entry must be exactly 1 character")
    if not ("A" <= letter <= "Z"):
        raise ValueError("entry must be a single letter A-Z")
    return letter


def main():
    validate(LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    print(LETTER)


if __name__ == "__main__":
    main()
