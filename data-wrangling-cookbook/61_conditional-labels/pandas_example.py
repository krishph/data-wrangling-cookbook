"""Assign labels with conditional logic — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    label = pd.Series("low", index=df.index)
    label = label.mask(df["score"] >= 70, "medium").mask(df["score"] >= 90, "high")
    result = df.assign(band=label)
    print(result)
    return result


if __name__ == "__main__":
    main()
