"""Filter groups using an aggregate threshold: Keep all transactions for customers whose total spending reaches a specified threshold."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    # Filter on a group total while retaining individual transaction rows.
    total = df.groupby("customer")["amount"].transform("sum")
    result = df.loc[total >= 100].sort_values("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
