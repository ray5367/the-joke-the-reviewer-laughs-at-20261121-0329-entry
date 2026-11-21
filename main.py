#!/usr/bin/env python3
"""Write one text to $MAKEFUN_OUTPUT_DIR/entry.txt: a one-line joke about
working beside an AI coding agent.

The joke is a fixed string, so the two grader runs are byte-identical: no
randomness, no clock reads, no network. It is built for the judge's brief:
the reviewer of the change is the butt of the joke, the setup runs a rule
of three (writes, reviews, approves), and the punchline lands on the human
reduced to a bystander on the incident report.
"""

import os

JOKE = (
    "My AI coding agent writes the code, reviews the code, and approves its "
    "own pull request — I'm just the human CC'd on the incident report."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(JOKE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
