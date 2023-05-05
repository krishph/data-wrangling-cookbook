"""Group by multiple dimensions — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.group_by("region", "product").agg(pl.col("quantity").sum().alias("total_units")).sort("region", "product")
    print(result)
    return result


if __name__ == "__main__":
    main()
