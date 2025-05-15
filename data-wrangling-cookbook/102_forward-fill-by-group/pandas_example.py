"""Carry observations forward within groups: Fill missing sensor readings from the latest earlier reading for the same sensor."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["timestamp"]).sort_values(["sensor", "timestamp"])
    # A leading missing reading stays missing; values never cross sensor boundaries.
    result = df.assign(filled_reading=df.groupby("sensor")["reading"].ffill())
    print(result)
    return result


if __name__ == "__main__":
    main()
