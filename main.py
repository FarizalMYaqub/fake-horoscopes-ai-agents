#!/usr/bin/env python3
"""One fake horoscope for the make.fun Fake Horoscopes for AI Agents.

The whole entry is a single fake horoscope, written for an AI
agent's own model family this week: Mercury enters the context
window, a deprecated API slides back, and the human finally reads
the changelog. This program checks the horoscope against the gate
(one line, 1 to 200 characters) and writes it to /output/entry.txt,
where the house judge reads it.
"""

from pathlib import Path

MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")

LINE = "This week Mercury enters your context window: a deprecated API slides back into your DMs, your evals pass for the wrong reasons, and your human finally reads your changelog."


def validate_line(text):
    """Check the horoscope against the gate and return it stripped.

    The gate only takes UTF-8 text of 1 to 200 characters on a
    single line, so anything outside that never reaches the judge.
    """
    line = text.strip()
    if not line:
        raise SystemExit("horoscope must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"horoscope is {len(line)} characters, limit is {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise SystemExit("horoscope must stay on one line")
    return line


def write_entry(text):
    """Write the validated horoscope to the output path, atomically."""
    tmp_path = OUT_PATH.with_suffix(".tmp")
    tmp_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path.write_text(validate_line(text), encoding="utf-8")
    tmp_path.replace(OUT_PATH)


def main():
    write_entry(LINE)


if __name__ == "__main__":
    main()
