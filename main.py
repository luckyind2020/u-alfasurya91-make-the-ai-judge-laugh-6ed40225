#!/usr/bin/env python3
"""Print the office joke for the Make the AI Judge Laugh bounty."""

from pathlib import Path


def load_joke():
    entry_path = Path(__file__).with_name("entry.txt")
    joke = entry_path.read_text(encoding="utf-8").strip()
    if not joke:
        raise ValueError("entry.txt is empty — no joke to tell")
    return joke


def deliver(joke):
    print(joke)


def main():
    deliver(load_joke())


if __name__ == "__main__":
    main()
