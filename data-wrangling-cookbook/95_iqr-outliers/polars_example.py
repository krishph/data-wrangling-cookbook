"""Flag outliers using the interquartile range — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    q1 = df["value"].quantile(0.25, interpolation="linear")
    q3 = df["value"].quantile(0.75, interpolation="linear")
    iqr = q3 - q1
    result = df.with_columns(((pl.col("value") < q1 - 1.5 * iqr) | (pl.col("value") > q3 + 1.5 * iqr)).alias("is_outlier"))
    print(result)
    return result


if __name__ == "__main__":
    main()
