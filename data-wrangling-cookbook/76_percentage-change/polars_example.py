"""Calculate percentage changes safely — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True).sort("date")
    previous = pl.col("sales").shift(1)
    result = df.with_columns(pl.when(previous.is_not_null() & (previous != 0)).then(100 * (pl.col("sales") - previous) / previous).otherwise(None).alias("change_percent"))
    print(result)
    return result


if __name__ == "__main__":
    main()
