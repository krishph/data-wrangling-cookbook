"""Calculate running totals by group — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["order_date"])
    result = df.sort_values(["customer", "order_date", "order_id"]).copy()
    result["running_units"] = result.groupby("customer")["quantity"].cumsum()
    print(result)
    return result


if __name__ == "__main__":
    main()
