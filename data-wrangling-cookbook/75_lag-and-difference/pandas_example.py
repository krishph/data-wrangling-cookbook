"""Compare a row with the previous row — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["date"]).sort_values("date")
    result = df.assign(previous_sales=df["sales"].shift(1), change=df["sales"].diff())
    print(result)
    return result


if __name__ == "__main__":
    main()
