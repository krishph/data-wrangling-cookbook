"""Select and rename columns — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df[["order_id", "customer", "quantity"]].rename(columns={"customer": "customer_name", "quantity": "units"})
    print(result)
    return result


if __name__ == "__main__":
    main()
