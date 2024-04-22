"""Keep all left-side rows when joining — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    result = orders.merge(customers, on="customer_id", how="left", validate="many_to_one", indicator=True)
    result["matched"] = result["_merge"].eq("both")
    result = result.drop(columns="_merge").sort_values("order_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
