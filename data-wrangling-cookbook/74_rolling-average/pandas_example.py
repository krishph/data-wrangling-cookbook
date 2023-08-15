"""Calculate a rolling moving average — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["date"]).sort_values("date")
    result = df.assign(moving_average=df["sales"].rolling(window=3, min_periods=1).mean())
    print(result)
    return result


if __name__ == "__main__":
    main()
