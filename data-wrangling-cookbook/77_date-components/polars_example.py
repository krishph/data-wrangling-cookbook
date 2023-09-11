"""Extract calendar features — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True)
    result = df.with_columns(pl.col("order_date").dt.year().alias("year"), pl.col("order_date").dt.month().alias("month"), pl.col("order_date").dt.weekday().alias("iso_weekday"))
    print(result)
    return result


if __name__ == "__main__":
    main()
