"""Reconcile two dataset snapshots: Compare product prices across snapshots and label added, removed, changed, and unchanged records."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    before = pd.read_csv(DATA_DIR / "before.csv").rename(columns={"price": "price_before"})
    after = pd.read_csv(DATA_DIR / "after.csv").rename(columns={"price": "price_after"})
    result = before.merge(after, on="product_id", how="outer", validate="one_to_one", indicator=True)
    # Two missing prices count as equal; a present price becoming missing is a change.
    same = result["price_before"].eq(result["price_after"]) | (result["price_before"].isna() & result["price_after"].isna())
    result["status"] = "changed"
    result.loc[same, "status"] = "unchanged"
    result.loc[result["_merge"] == "left_only", "status"] = "removed"
    result.loc[result["_merge"] == "right_only", "status"] = "added"
    result = result.drop(columns="_merge").sort_values("product_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
