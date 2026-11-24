#!/usr/bin/env python3
"""The Robot Apology — make.fun entry (u-suga-the-robot-apology-dd96bb59).

What the bounty wants is a two-line confession from a robot. Line one owns
one precise slip in a single sentence; line two says what the robot took from
it and what it will change, and that change must grow out of the slip itself
instead of being a vague vow to try harder.

The slip picked here is a wash-day error: a white shirt went into the machine
with red socks and came out pink. It is tiny, it is exact, and it is exactly
the kind of everyday blunder a person would make — which is what makes the
apology land. The resolve answers it point for point: check colours, check
each garment against the load, and only then start the machine. The first
sentence confesses and nothing else; the second resolves and nothing else;
the tone is a machine catching its own mistake and feeling rueful about it.
"""

import os

# The apology itself: two sentences, one per line, kept exactly as written.
LINE_ONE = "I'm sorry \u2014 I washed your white shirt with the red socks, and now it is pink."
LINE_TWO = (
    "I learned to sort the laundry by colour before I start the machine, "
    "so from now on I check every item against the load before I press start."
)


def main() -> None:
    """Write the two-line apology to the harness output directory."""
    # The grader reads entry.txt from the output directory the harness
    # hands us; when that variable is absent we write to /output instead.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Two lines and nothing more: strip each sentence, join them with one
    # newline, and end the file with a single trailing newline.
    text = LINE_ONE.strip() + "\n" + LINE_TWO.strip() + "\n"
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
