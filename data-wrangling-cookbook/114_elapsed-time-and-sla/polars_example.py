"""Calculate elapsed time and flag overdue work: Measure ticket resolution time in hours and flag completed tickets exceeding a 24-hour target."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True)
    result = df.with_columns(((pl.col("closed_at") - pl.col("opened_at")).dt.total_seconds() / 3600).alias("resolution_hours"))
    # A null closure stays null; exactly 24 hours does not breach this target.
    result = result.with_columns((pl.col("resolution_hours") > 24).alias("breached"))
    print(result)
    return result


if __name__ == "__main__":
    main()
