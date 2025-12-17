"""Reconcile two dataset snapshots: Compare product prices across snapshots and label added, removed, changed, and unchanged records."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    before = pl.read_csv(DATA_DIR / "before.csv").rename({"price": "price_before"}).with_columns(pl.lit(True).alias("in_before"))
    after = pl.read_csv(DATA_DIR / "after.csv").rename({"price": "price_after"}).with_columns(pl.lit(True).alias("in_after"))
    result = before.join(after, on="product_id", how="full", coalesce=True, validate="1:1")
    # Presence markers distinguish absent records from records with missing prices.
    result = result.with_columns(
        pl.when(pl.col("in_before").is_null()).then(pl.lit("added"))
        .when(pl.col("in_after").is_null()).then(pl.lit("removed"))
        .when(pl.col("price_before").eq_missing(pl.col("price_after"))).then(pl.lit("unchanged"))
        .otherwise(pl.lit("changed")).alias("status")
    ).drop("in_before", "in_after").sort("product_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
