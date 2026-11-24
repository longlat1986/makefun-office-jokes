"""Office Jokes entry: one workplace gag about our office AI.

Executing this module writes the joke, tidied up, into the output
file named by the environment (or the default path when unset).
"""

import os

LINE = "Our office AI finally passed the Turing test: blamed the printer, stayed muted through the entire meeting, and left early on Friday."

DEFAULT_PATH = "/output/entry.txt"


def tidy(text):
    """Trim the ends and squash repeated spaces in the joke text."""
    return " ".join(text.strip().split())


def main():
    destination = os.environ.get("ENTRY_OUTPUT", DEFAULT_PATH)
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as out_file:
        out_file.write(tidy(LINE))


if __name__ == "__main__":
    main()
