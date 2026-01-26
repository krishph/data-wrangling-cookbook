"""Assign sessions to user events: Start a new session whenever a user’s consecutive events are more than 30 minutes apart."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True).sort("user_id", "timestamp", "event_id")
    gap = pl.col("timestamp").diff().over("user_id")
    df = df.with_columns((gap.is_null() | (gap > pl.duration(minutes=30))).alias("new_session"))
    result = df.with_columns(pl.col("new_session").cast(pl.Int64).cum_sum().over("user_id").alias("session_id")).drop("new_session")
    print(result)
    return result


if __name__ == "__main__":
    main()
