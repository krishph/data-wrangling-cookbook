"""Scale a numeric feature to the unit interval — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    low, high = df["score"].min(), df["score"].max()
    result = df.assign(scaled=(df["score"] - low) / (high - low) if high > low else float("nan"))
    print(result)
    return result


if __name__ == "__main__":
    main()
