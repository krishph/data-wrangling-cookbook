"""Summarize distributions with group percentiles: Calculate median and 90th-percentile response times for each service using linear interpolation."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.groupby("service", as_index=False).agg(
        median_ms=("latency_ms", "median"),
        p90_ms=("latency_ms", lambda values: values.quantile(0.9, interpolation="linear")),
    ).sort_values("service")
    print(result)
    return result


if __name__ == "__main__":
    main()
