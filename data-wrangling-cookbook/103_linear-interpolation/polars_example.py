"""Interpolate gaps between observations: Estimate missing readings between known values in an evenly spaced time series."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv").sort("minute")
    # Linear interpolation leaves leading and trailing nulls unchanged.
    result = df.with_columns(pl.col("temperature").interpolate().alias("interpolated"))
    print(result)
    return result


if __name__ == "__main__":
    main()
