"""Assign labels with conditional logic — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.when(pl.col("score") >= 90).then(pl.lit("high")).when(pl.col("score") >= 70).then(pl.lit("medium")).otherwise(pl.lit("low")).alias("band"))
    print(result)
    return result


if __name__ == "__main__":
    main()
