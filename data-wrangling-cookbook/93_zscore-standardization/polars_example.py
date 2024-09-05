"""Standardize a numeric feature with z-scores — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    std = pl.col("score").std(ddof=0)
    result = df.with_columns(pl.when(std > 0).then((pl.col("score") - pl.col("score").mean()) / std).otherwise(None).alias("z_score"))
    print(result)
    return result


if __name__ == "__main__":
    main()
