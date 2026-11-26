#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes one original fortune cookie message for a software engineer to
``entry.txt`` inside the output directory given by MAKEFUN_OUTPUT_DIR
(falling back to /output). Python standard library only; deterministic.
"""

import os

FORTUNE = "Your manager will demo the one bug you could never reproduce."


def main() -> None:
    # The gate requires 1 to 120 characters; keep the fortune inside it.
    assert 1 <= len(FORTUNE) <= 120, "fortune must be 1-120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
