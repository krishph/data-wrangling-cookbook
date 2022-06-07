"""Read a CSV and inspect its schema — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    print(df.schema)
    result = df.head(3)
    print(result)
    return result


if __name__ == "__main__":
    main()
