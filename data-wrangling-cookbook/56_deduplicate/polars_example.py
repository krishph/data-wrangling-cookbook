"""Keep the latest record per key — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True)
    result = df.sort("updated_at").unique(subset=["customer_id"], keep="last").sort("customer_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
