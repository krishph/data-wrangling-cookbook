"""Measure correlation between two columns — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv").dropna(subset=["ad_spend", "revenue"])
    result = pd.DataFrame({"pearson_r": [df["ad_spend"].corr(df["revenue"], method="pearson")]})
    print(result)
    return result


if __name__ == "__main__":
    main()
