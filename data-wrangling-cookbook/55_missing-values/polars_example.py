"""Fill missing numeric and categorical values — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.col("age").fill_null(pl.col("age").median()), pl.col("city").fill_null("Unknown"))
    print(result)
    return result


if __name__ == "__main__":
    main()
