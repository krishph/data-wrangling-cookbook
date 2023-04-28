"""Aggregate totals and averages by group — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.group_by("region").agg(pl.len().alias("orders"), pl.col("quantity").sum().alias("total_units"), pl.col("quantity").mean().alias("average_units")).sort("region")
    print(result)
    return result


if __name__ == "__main__":
    main()
