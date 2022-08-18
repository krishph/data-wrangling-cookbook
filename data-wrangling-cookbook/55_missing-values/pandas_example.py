"""Fill missing numeric and categorical values — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(age=df["age"].fillna(df["age"].median()), city=df["city"].fillna("Unknown"))
    print(result)
    return result


if __name__ == "__main__":
    main()
