"""Build a complete category grid: Create every store/product combination and fill unobserved sales combinations with zero."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    stores = pd.read_csv(DATA_DIR / "stores.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    sales = pd.read_csv(DATA_DIR / "sales.csv")
    grid = stores.merge(products, how="cross")
    # The sample has unique dimensions and one sales row per store/product pair.
    result = grid.merge(sales, on=["store", "product"], how="left", validate="one_to_one")
    result["units"] = result["units"].fillna(0).astype("int64")
    result = result.sort_values(["store", "product"])
    print(result)
    return result


if __name__ == "__main__":
    main()
