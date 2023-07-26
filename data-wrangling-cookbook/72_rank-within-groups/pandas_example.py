"""Rank values within groups — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(rank=df.groupby("team")["score"].rank(method="dense", ascending=False).astype("int64"))
    result = result.sort_values(["team", "rank", "employee"])
    print(result)
    return result


if __name__ == "__main__":
    main()
