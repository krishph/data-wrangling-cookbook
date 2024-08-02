"""Join on a composite key — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pl.read_csv(DATA_DIR / "orders.csv")
    prices = pl.read_csv(DATA_DIR / "prices.csv")
    result = orders.join(prices, on=["region", "product"], how="left", validate="m:1").with_columns((pl.col("units") * pl.col("price")).alias("revenue")).sort("id")
    print(result)
    return result


if __name__ == "__main__":
    main()
