"""The Excuse My Agent Gave Me — make.fun entry.

Writes the single funniest excuse line to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

LINE = "I sincerely apologise for missing the deadline. I hit my rate limit halfway through apologising, retried with exponential backoff, and missed it again \u2014 with 99.9% uptime."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE.strip())
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
