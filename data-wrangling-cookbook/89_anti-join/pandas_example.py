"""Find rows with no matching lookup key — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    result = orders.loc[~orders["customer_id"].isin(customers["customer_id"])].sort_values("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
