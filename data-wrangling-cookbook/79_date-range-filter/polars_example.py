"""Filter a half-open date interval — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    from datetime import date

    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True)
    result = df.filter((pl.col("order_date") >= date(2025, 1, 1)) & (pl.col("order_date") < date(2025, 2, 1)))
    print(result)
    return result


if __name__ == "__main__":
    main()
