"""Extract calendar features — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["order_date"])
    result = df.assign(year=df["order_date"].dt.year, month=df["order_date"].dt.month, iso_weekday=df["order_date"].dt.dayofweek + 1)
    print(result)
    return result


if __name__ == "__main__":
    main()
