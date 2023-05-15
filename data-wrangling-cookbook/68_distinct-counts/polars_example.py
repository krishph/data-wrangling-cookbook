"""Count unique values within each group — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.group_by("region").agg(pl.col("customer").drop_nulls().n_unique().alias("unique_customers")).sort("region")
    print(result)
    return result


if __name__ == "__main__":
    main()
