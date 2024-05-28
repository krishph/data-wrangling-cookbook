"""Find rows with no matching lookup key — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pl.read_csv(DATA_DIR / "orders.csv")
    customers = pl.read_csv(DATA_DIR / "customers.csv")
    result = orders.join(customers, on="customer_id", how="anti").sort("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
