"""Scale a numeric feature to the unit interval — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    low, high = pl.col("score").min(), pl.col("score").max()
    result = df.with_columns(pl.when(high > low).then((pl.col("score") - low) / (high - low)).otherwise(None).alias("scaled"))
    print(result)
    return result


if __name__ == "__main__":
    main()
