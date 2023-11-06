"""Fill missing dates in a daily series — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True)
    calendar = pl.DataFrame({"date": pl.date_range(df["date"].min(), df["date"].max(), interval="1d", eager=True)})
    result = calendar.join(df, on="date", how="left", validate="1:1").with_columns(pl.col("sales").fill_null(0)).sort("date")
    print(result)
    return result


if __name__ == "__main__":
    main()
