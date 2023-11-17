"""Convert UTC timestamps to local time — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.col("timestamp").str.to_datetime(time_zone="UTC").alias("utc_time"))
    result = result.with_columns(pl.col("utc_time").dt.convert_time_zone("America/New_York").alias("new_york_time"))
    print(result)
    return result


if __name__ == "__main__":
    main()
