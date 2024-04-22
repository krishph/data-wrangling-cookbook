"""Keep all left-side rows when joining — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pl.read_csv(DATA_DIR / "orders.csv")
    customers = pl.read_csv(DATA_DIR / "customers.csv").with_columns(pl.lit(True).alias("matched"))
    result = orders.join(customers, on="customer_id", how="left", validate="m:1").with_columns(pl.col("matched").fill_null(False)).sort("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
