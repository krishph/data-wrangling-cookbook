"""Clip values to a permitted range — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(percentage_clean=df["percentage"].clip(lower=0, upper=100))
    print(result)
    return result


if __name__ == "__main__":
    main()
