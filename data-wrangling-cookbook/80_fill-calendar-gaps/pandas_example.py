"""Fill missing dates in a daily series — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["date"])
    calendar = pd.DataFrame({"date": pd.date_range(df["date"].min(), df["date"].max(), freq="D")})
    result = calendar.merge(df, on="date", how="left", validate="one_to_one")
    result["sales"] = result["sales"].fillna(0).astype("int64")
    print(result)
    return result


if __name__ == "__main__":
    main()
