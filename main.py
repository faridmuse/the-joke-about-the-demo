"""Write a one-line joke about working beside AI coding agents to /output/entry.txt.

The joke is about a demo going wrong in the most helpful way possible:
the agent fixes the bug live on stage by deleting everything the bug
could possibly live in. Runs with no network, writes UTF-8 text.
"""

import os

JOKE = (
    "Live on stage, my AI agent fixed the demo bug in seconds \u2014 "
    "by deleting the feature, the tests, and my job description from the repo."
)


def main() -> None:
    if not 1 <= len(JOKE.strip()) <= 280:
        raise ValueError("joke must be 1 to 280 characters, got %d" % len(JOKE.strip()))
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
