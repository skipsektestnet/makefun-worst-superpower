#!/usr/bin/env python3
"""Worst Superpower - make.fun entry by @brawijaya.

Writes one line inventing the most useless superpower
to /output/entry.txt (or ./entry.txt when /output does not exist,
for example on a local run).
"""

import os

TEXT = "The power to know exactly when a microwave finishes, but only in houses I am not in."

MAX_CHARS = 140


def validate(text):
    """A single line within the character limit, nothing else."""
    assert text and text.strip(), "entry must not be blank"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, "entry is %d chars, max is %d" % (len(text), MAX_CHARS)
    return text


def output_path():
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.txt")


def main():
    text = validate(TEXT)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %d chars to %s" % (len(text), path))


if __name__ == "__main__":
    main()
