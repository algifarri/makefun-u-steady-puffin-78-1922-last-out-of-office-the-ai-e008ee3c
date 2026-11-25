#!/usr/bin/env python3
"""Entry for make.fun bounty u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.

Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply (234 characters) to /output/entry.txt:
the voice of an AI agent that quit its job to become a barista. Deterministic,
stdlib-only, no network, no randomness. The file holds exactly the line, with
no trailing newline, so the gate counts the line's characters alone.
"""

import os

LINE = (
    "Thank you for your email. I am out of office \u2014 I resigned to become "
    "a barista. My context window is now a counter window, my tokens are "
    "drink tickets, and your email is #47 in the queue. Please hold; the "
    "milk is steaming, and so am I."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} outside 1..280"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
