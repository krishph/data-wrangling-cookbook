"""Flatten nested JSON records: Expand nested customer details into ordinary columns while preserving one row per order."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    import json

    records = json.loads((DATA_DIR / "data.json").read_text())
    result = pd.json_normalize(records).rename(columns={"customer.customer_id": "customer_id", "customer.city": "city"})
    result = result[["order_id", "customer_id", "city", "amount"]]
    print(result)
    return result


if __name__ == "__main__":
    main()
