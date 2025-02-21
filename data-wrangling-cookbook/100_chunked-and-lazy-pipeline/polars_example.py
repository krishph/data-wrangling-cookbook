"""Process a CSV with chunks or a lazy query — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    query = (
        pl.scan_csv(DATA_DIR / "data.csv")
        .filter(pl.col("quantity") >= 2)
        .with_columns((pl.col("quantity") * pl.col("unit_price")).alias("revenue"))
        .group_by("region")
        .agg(pl.col("revenue").sum())
        .sort("region")
    )
    result = query.collect()
    print(result)
    return result


if __name__ == "__main__":
    main()
