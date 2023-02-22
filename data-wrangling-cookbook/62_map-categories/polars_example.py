"""Map codes to readable categories — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    lookup = {"N": "New", "S": "Shipped", "C": "Cancelled"}
    result = df.with_columns(pl.col("status").replace_strict(lookup, default="Unknown").alias("status_name"))
    print(result)
    return result


if __name__ == "__main__":
    main()
