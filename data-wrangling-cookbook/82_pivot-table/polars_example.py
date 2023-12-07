"""Pivot long data into a summary table — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.pivot(on="product", index="region", values="quantity", aggregate_function="sum").fill_null(0).select("region", "Book", "Folder", "Pen").sort("region")
    print(result)
    return result


if __name__ == "__main__":
    main()
