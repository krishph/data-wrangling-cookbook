"""Calculate a weighted average — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.group_by("product").agg(pl.col("units").sum(), (pl.col("units") * pl.col("price")).sum().alias("revenue"))
    result = result.with_columns(pl.when(pl.col("units") != 0).then(pl.col("revenue") / pl.col("units")).otherwise(None).alias("weighted_price")).sort("product")
    print(result)
    return result


if __name__ == "__main__":
    main()
