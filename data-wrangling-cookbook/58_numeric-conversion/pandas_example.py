"""Convert messy numeric strings — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    clean = df["amount"].str.replace(r"[$,]", "", regex=True)
    result = df.assign(amount=pd.to_numeric(clean, errors="coerce"))
    print(result)
    return result


if __name__ == "__main__":
    main()
