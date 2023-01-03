"""Parse dates and handle invalid input — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(date=pd.to_datetime(df["date_text"], format="%Y-%m-%d", errors="coerce"))
    print(result)
    return result


if __name__ == "__main__":
    main()
