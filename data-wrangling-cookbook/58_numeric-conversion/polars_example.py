"""Convert messy numeric strings — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.col("amount").str.replace_all(r"[$,]", "").cast(pl.Float64, strict=False))
    print(result)
    return result


if __name__ == "__main__":
    main()
