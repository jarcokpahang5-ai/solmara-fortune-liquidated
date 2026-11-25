"""Fortune Cookie for the Liquidated Trader -- make.fun entry.

One fortune-cookie line, at most 20 words, for a crypto trader just
liquidated: it sounds like a real fortune and lands as a joke on the
loss. The program validates the word count, prints the fortune, and
writes it to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

FORTUNE = (
    "Your next trade will be brilliant. Unfortunately, it will be "
    "brilliant for someone else."
)

MAX_WORDS = 20
TARGET = "/output/entry.txt"


def word_count(text):
    return len(text.split())


def check_fortune(fortune):
    """One line, at most MAX_WORDS words, ending with a period."""
    if not isinstance(fortune, str) or not fortune:
        raise ValueError("entry must be non-empty text")
    if "\n" in fortune:
        raise ValueError("entry must be exactly one line")
    if fortune != fortune.strip():
        raise ValueError("entry must not start or end with whitespace")
    words = word_count(fortune)
    if words > MAX_WORDS:
        raise ValueError(
            "entry has %d words, must be at most %d" % (words, MAX_WORDS)
        )
    if words < 5:
        raise ValueError("entry is too short to be a fortune")
    if not fortune.endswith("."):
        raise ValueError("entry must end with a period")
    if fortune.count(".") < 2:
        raise ValueError("entry needs a fortune sentence and a twist sentence")
    return fortune


def check_fortune_shape(fortune):
    """A fortune predicts the future and then twists it."""
    if "will" not in fortune.lower():
        raise ValueError("entry must predict something with 'will'")
    if "unfortunately" not in fortune.lower():
        raise ValueError("entry must carry the twist")
    return fortune


def main():
    fortune = check_fortune_shape(check_fortune(FORTUNE))
    print(fortune)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(fortune + "\n")


if __name__ == "__main__":
    main()
