"""Calculate running totals by group — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True)
    result = df.sort("customer", "order_date", "order_id").with_columns(pl.col("quantity").cum_sum().over("customer").alias("running_units"))
    print(result)
    return result


if __name__ == "__main__":
    main()
