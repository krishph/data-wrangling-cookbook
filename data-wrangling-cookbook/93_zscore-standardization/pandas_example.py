"""Standardize a numeric feature with z-scores — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    std = df["score"].std(ddof=0)
    denominator = std if pd.notna(std) and std != 0 else float("nan")
    result = df.assign(z_score=(df["score"] - df["score"].mean()) / denominator)
    print(result)
    return result


if __name__ == "__main__":
    main()
