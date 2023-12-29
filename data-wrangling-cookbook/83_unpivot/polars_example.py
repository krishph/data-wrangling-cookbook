"""Unpivot wide data into tidy rows — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.unpivot(index="store", on=["Jan", "Feb", "Mar"], variable_name="month", value_name="sales").sort("store", "month")
    print(result)
    return result


if __name__ == "__main__":
    main()
