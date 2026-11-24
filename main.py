#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes a single original one-line weather forecast (136 chars,
inside the 140-character limit) for Wobblewick, a city that does
not exist, to /output/entry.txt. Deterministic: the same line every
run, no network, no file reads, Python 3.13 stdlib only.
"""

import os

FORECAST = (
    "Wobblewick: drizzle at 14°, the 7 bus on time for once, "
    "and pigeons sharing umbrellas — grab a brolly, commuter, it's your lucky Tuesday."
)

OUTPUT_PATH = os.path.join("/output", "entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(FORECAST)


if __name__ == "__main__":
    main()
