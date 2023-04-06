"""Flag records that violate data rules — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.col("age").is_between(0, 120).fill_null(False).alias("valid_age"), pl.col("email").str.contains(r"^[^@\s]+@[^@\s]+\.[^@\s]+$").fill_null(False).alias("valid_email"))
    result = result.with_columns((pl.col("valid_age") & pl.col("valid_email")).alias("is_valid"))
    print(result)
    return result


if __name__ == "__main__":
    main()
