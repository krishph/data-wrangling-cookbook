"""Replace sentinel values with missing values — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(temperature=df["temperature"].mask(df["temperature"] == -999))
    print("Mean temperature:", result["temperature"].mean())
    print(result)
    return result


if __name__ == "__main__":
    main()
