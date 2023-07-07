"""Build a frequency and percentage table — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.group_by("priority").agg(pl.len().alias("count"))
    result = result.with_columns((100 * pl.col("count") / pl.col("count").sum()).round(2).alias("percent")).sort(["count", "priority"], descending=[True, False])
    print(result)
    return result


if __name__ == "__main__":
    main()
