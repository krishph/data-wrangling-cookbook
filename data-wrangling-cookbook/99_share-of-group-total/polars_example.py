"""Calculate each row’s share of a group total — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns((pl.col("quantity") * pl.col("unit_price")).alias("revenue"))
    result = result.with_columns(pl.col("revenue").sum().over("region").alias("region_revenue"))
    result = result.with_columns(pl.when(pl.col("region_revenue") != 0).then(100 * pl.col("revenue") / pl.col("region_revenue")).otherwise(None).alias("percent_of_region"))
    print(result)
    return result


if __name__ == "__main__":
    main()
