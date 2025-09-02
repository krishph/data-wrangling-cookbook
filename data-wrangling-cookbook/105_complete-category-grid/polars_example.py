"""Build a complete category grid: Create every store/product combination and fill unobserved sales combinations with zero."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    stores = pl.read_csv(DATA_DIR / "stores.csv")
    products = pl.read_csv(DATA_DIR / "products.csv")
    sales = pl.read_csv(DATA_DIR / "sales.csv")
    grid = stores.join(products, how="cross")
    # Zero means no sales here, rather than unknown sales.
    result = grid.join(sales, on=["store", "product"], how="left", validate="1:1").with_columns(pl.col("units").fill_null(0)).sort("store", "product")
    print(result)
    return result


if __name__ == "__main__":
    main()
