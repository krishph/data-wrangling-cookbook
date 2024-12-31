"""Extract structured values from text — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    order = df["message"].str.extract(r"Order #(\d+)", expand=False)
    amount = df["message"].str.extract(r"\$(\d+(?:\.\d+)?)", expand=False)
    result = df.assign(order_id=pd.to_numeric(order, errors="coerce").astype("Int64"), amount=pd.to_numeric(amount, errors="coerce"))
    print(result)
    return result


if __name__ == "__main__":
    main()
