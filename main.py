#!/usr/bin/env python3
"""Entry for make.fun bounty u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
The roast targets the fridge's camera, app, firmware, and ice maker.
"""

import os

TEXT = "My fridge has a camera, an app, and a firmware update due — all that technology, and it still can't make ice without announcing it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
