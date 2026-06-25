"""Parse multiple known date formats: Combine explicit parsers for ISO and US-style dates while leaving invalid values missing."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    iso = pd.to_datetime(df["date_text"], format="%Y-%m-%d", errors="coerce")
    us = pd.to_datetime(df["date_text"], format="%m/%d/%Y", errors="coerce")
    # The slash format is explicitly month/day/year: 03/04 means March 4.
    result = df.assign(parsed_date=iso.combine_first(us))
    print(result)
    return result


if __name__ == "__main__":
    main()
