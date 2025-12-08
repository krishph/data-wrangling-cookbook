"""Filter groups using an aggregate threshold: Keep all transactions for customers whose total spending reaches a specified threshold."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.filter(pl.col("amount").sum().over("customer") >= 100).sort("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
