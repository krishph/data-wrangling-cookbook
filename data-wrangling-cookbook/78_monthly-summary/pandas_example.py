"""Aggregate daily records into months — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["order_date"])
    df["month"] = df["order_date"].dt.to_period("M").dt.to_timestamp()
    result = df.groupby("month", as_index=False).agg(total_units=("quantity", "sum")).sort_values("month")
    print(result)
    return result


if __name__ == "__main__":
    main()
