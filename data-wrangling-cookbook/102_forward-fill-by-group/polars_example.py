"""Carry observations forward within groups: Fill missing sensor readings from the latest earlier reading for the same sensor."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True).sort("sensor", "timestamp")
    # Forward filling assumes a reading remains valid until the next observation.
    result = df.with_columns(pl.col("reading").forward_fill().over("sensor").alias("filled_reading"))
    print(result)
    return result


if __name__ == "__main__":
    main()
