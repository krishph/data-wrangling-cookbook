"""Count consecutive value streaks: Number runs of repeated statuses and count each row’s position within its run."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv").sort("day")
    new_run = (pl.col("status") != pl.col("status").shift()).fill_null(True)
    df = df.with_columns(new_run.cast(pl.Int64).cum_sum().alias("run_id"))
    result = df.with_columns(pl.col("status").cum_count().over("run_id").alias("streak_length"))
    print(result)
    return result


if __name__ == "__main__":
    main()
