"""Calculate each row’s share of a group total — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    df["revenue"] = df["quantity"] * df["unit_price"]
    total = df.groupby("region")["revenue"].transform("sum")
    result = df.assign(region_revenue=total, percent_of_region=100 * df["revenue"] / total.where(total != 0))
    print(result)
    return result


if __name__ == "__main__":
    main()
