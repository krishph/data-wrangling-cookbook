"""Summarize distributions with group percentiles: Calculate median and 90th-percentile response times for each service using linear interpolation."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.group_by("service").agg(
        pl.col("latency_ms").median().alias("median_ms"),
        pl.col("latency_ms").quantile(0.9, interpolation="linear").alias("p90_ms"),
    ).sort("service")
    print(result)
    return result


if __name__ == "__main__":
    main()
