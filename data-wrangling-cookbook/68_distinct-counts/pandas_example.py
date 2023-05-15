"""Count unique values within each group — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.groupby("region", as_index=False).agg(unique_customers=("customer", "nunique")).sort_values("region")
    print(result)
    return result


if __name__ == "__main__":
    main()
