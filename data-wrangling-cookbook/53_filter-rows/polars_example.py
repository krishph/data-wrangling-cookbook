"""Filter rows using multiple conditions — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.filter((pl.col("region") == "East") & (pl.col("quantity") >= 3))
    print(result)
    return result


if __name__ == "__main__":
    main()
