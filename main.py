import os

LINE = "Our office AI finally passed the Turing test: blamed the printer, stayed muted through the entire meeting, and left early on Friday."


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
