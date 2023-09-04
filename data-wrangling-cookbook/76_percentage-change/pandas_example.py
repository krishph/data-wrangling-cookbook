"""Calculate percentage changes safely — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["date"]).sort_values("date")
    previous = df["sales"].shift(1)
    result = df.assign(change_percent=100 * (df["sales"] - previous) / previous.where(previous != 0))
    print(result)
    return result


if __name__ == "__main__":
    main()
