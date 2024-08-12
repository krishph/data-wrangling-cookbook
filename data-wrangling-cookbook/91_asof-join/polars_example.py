"""Match the most recent earlier observation — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    trades = pl.read_csv(DATA_DIR / "trades.csv", try_parse_dates=True).sort("time")
    quotes = pl.read_csv(DATA_DIR / "quotes.csv", try_parse_dates=True).sort("time")
    result = trades.join_asof(quotes, on="time", strategy="backward", tolerance="5s")
    print(result)
    return result


if __name__ == "__main__":
    main()
