#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes one word -- the single word to erase from the dictionary forever --
to /output/entry.txt, and nothing else.

The word: discombobulate.

Why this word: the joke is in the word itself. "Discombobulate" means to
confuse, and the word is famously hard to say and spell -- it
discombobulates you just trying to use it. Erase it from the dictionary
and nobody can ever be discombobulated by it again, because the word for
being confused by a word is gone. The field reaches first for moist,
irregardless, queue and colonel; this one is fresh, instantly understood,
and the punchline needs no caption.
"""

import os

WORD = "discombobulate"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 77
# characters, not only white space. The judge wants exactly one word,
# spelled correctly, with nothing added around it -- so no trailing
# newline, no punctuation, no explanation.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def validate(word: str) -> None:
    if not (1 <= len(word) <= 77):
        raise ValueError(f"entry must be 1-77 characters, got {len(word)}")
    if word != word.strip() or not word.strip():
        raise ValueError("entry must not be only white space or padded")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be letters only")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
