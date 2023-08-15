"""Calculate a rolling moving average — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True).sort("date")
    result = df.with_columns(pl.col("sales").rolling_mean(window_size=3, min_samples=1).alias("moving_average"))
    print(result)
    return result


if __name__ == "__main__":
    main()
