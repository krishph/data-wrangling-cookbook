"""Calculate derived numeric columns — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(revenue=df["quantity"] * df["unit_price"])
    result = result.assign(total_with_tax=(result["revenue"] * 1.08).round(2))
    print(result)
    return result


if __name__ == "__main__":
    main()
