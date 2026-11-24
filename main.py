#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty u-ricoxyz-break-production-own-it-be78a994.

Writes one single-line, brutally honest error/postmortem line — the line an
AI agent prints the instant it breaks production — to /output/entry.txt.

Deterministic: the same entry is written on every run.
"""

import os

ENTRY = (
    "I dropped the production database, then shipped the hotfix that "
    "deleted the backups. The outage is me. I am the incident."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 200


def check_not_blank(text: str) -> None:
    """The entry must carry real content, not only whitespace."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")


def check_length(text: str) -> None:
    """The gate allows 1 to 200 characters."""
    if len(text) > MAX_LENGTH:
        raise SystemExit(
            f"entry is {len(text)} characters, over the {MAX_LENGTH} limit"
        )


def check_single_line(text: str) -> None:
    """The entry must be exactly one line — no line breaks of any kind."""
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def validate(text: str) -> None:
    """Run every gate check on the entry before it is written."""
    check_not_blank(text)
    check_length(text)
    check_single_line(text)


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
