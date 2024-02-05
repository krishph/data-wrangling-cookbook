"""Expand delimited values into rows — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.col("tags").str.split("|").alias("tag")).explode("tag").drop("tags")
    print(result)
    return result


if __name__ == "__main__":
    main()
