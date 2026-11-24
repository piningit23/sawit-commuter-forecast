# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/piningit23/sawit-commuter-forecast/rank.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/piningit23/sawit-commuter-forecast/reward.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the [make.fun bounty](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
`u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e`.

## What it does

`main.py` writes one original line of weather forecast (137 characters,
inside the 140-character limit) for a city that does not exist to
`/output/entry.txt`. The forecast is for Wobblewick: drizzle at 14°,
the 7 bus on time for once, and pigeons sharing umbrellas — with a word
for the bored commuter at the bus stop.

The program is deterministic: two runs produce byte-identical
output. Python 3.13 standard library only, no network access, no
file reads.

## How to run

```sh
python3 main.py
```

This creates `/output` if needed and writes `/output/entry.txt`.
