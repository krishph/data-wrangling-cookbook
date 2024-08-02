"""Join on a composite key — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    orders = pd.read_csv(DATA_DIR / "orders.csv")
    prices = pd.read_csv(DATA_DIR / "prices.csv")
    result = orders.merge(prices, on=["region", "product"], how="left", validate="many_to_one")
    result["revenue"] = result["units"] * result["price"]
    result = result.sort_values("id")
    print(result)
    return result


if __name__ == "__main__":
    main()
