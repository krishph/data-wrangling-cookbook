"""Keep records whose keys exist in another table: Select orders from eligible customers without adding lookup columns or multiplying rows."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pl.read_csv(DATA_DIR / "orders.csv")
    eligible = pl.read_csv(DATA_DIR / "eligible.csv")
    result = orders.join(eligible, on="customer_id", how="semi").sort("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
