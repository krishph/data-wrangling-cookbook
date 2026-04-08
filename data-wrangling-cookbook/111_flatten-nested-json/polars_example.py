"""Flatten nested JSON records: Expand nested customer details into ordinary columns while preserving one row per order."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_json(DATA_DIR / "data.json")
    # Customer is a struct with field names that do not collide with outer columns.
    result = df.unnest("customer").select("order_id", "customer_id", "city", "amount")
    print(result)
    return result


if __name__ == "__main__":
    main()
