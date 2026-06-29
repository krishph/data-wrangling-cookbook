"""Parse multiple known date formats: Combine explicit parsers for ISO and US-style dates while leaving invalid values missing."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.coalesce(
        pl.col("date_text").str.strptime(pl.Date, format="%Y-%m-%d", strict=False),
        pl.col("date_text").str.strptime(pl.Date, format="%m/%d/%Y", strict=False),
    ).alias("parsed_date"))
    print(result)
    return result


if __name__ == "__main__":
    main()
