"""Compare a row with the previous row — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True).sort("date")
    result = df.with_columns(pl.col("sales").shift(1).alias("previous_sales"), pl.col("sales").diff().alias("change"))
    print(result)
    return result


if __name__ == "__main__":
    main()
