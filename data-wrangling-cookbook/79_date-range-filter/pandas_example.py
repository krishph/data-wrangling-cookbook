"""Filter a half-open date interval — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["order_date"])
    result = df.loc[(df["order_date"] >= pd.Timestamp("2025-01-01")) & (df["order_date"] < pd.Timestamp("2025-02-01"))]
    print(result)
    return result


if __name__ == "__main__":
    main()
