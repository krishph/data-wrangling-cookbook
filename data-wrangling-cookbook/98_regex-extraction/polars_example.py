"""Extract structured values from text — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.col("message").str.extract(r"Order #(\d+)", 1).cast(pl.Int64, strict=False).alias("order_id"), pl.col("message").str.extract(r"\$(\d+(?:\.\d+)?)", 1).cast(pl.Float64, strict=False).alias("amount"))
    print(result)
    return result


if __name__ == "__main__":
    main()
