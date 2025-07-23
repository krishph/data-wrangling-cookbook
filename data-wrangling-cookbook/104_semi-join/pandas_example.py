"""Keep records whose keys exist in another table: Select orders from eligible customers without adding lookup columns or multiplying rows."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    eligible = pd.read_csv(DATA_DIR / "eligible.csv")
    # Duplicate keys in the eligibility list must not duplicate orders.
    result = orders.loc[orders["customer_id"].isin(eligible["customer_id"])].sort_values("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
