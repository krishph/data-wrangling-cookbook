"""Measure correlation between two columns — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv").drop_nulls(["ad_spend", "revenue"])
    result = df.select(pl.corr("ad_spend", "revenue", method="pearson").alias("pearson_r"))
    print(result)
    return result


if __name__ == "__main__":
    main()
