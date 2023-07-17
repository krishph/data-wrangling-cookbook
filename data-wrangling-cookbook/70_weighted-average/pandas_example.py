"""Calculate a weighted average — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    df["revenue"] = df["units"] * df["price"]
    result = df.groupby("product", as_index=False).agg(units=("units", "sum"), revenue=("revenue", "sum"))
    result["weighted_price"] = result["revenue"] / result["units"].where(result["units"] != 0)
    result = result.sort_values("product")
    print(result)
    return result


if __name__ == "__main__":
    main()
