"""Keep the latest record per key — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["updated_at"])
    result = df.sort_values("updated_at").drop_duplicates("customer_id", keep="last").sort_values("customer_id")
    print(result)
    return result


if __name__ == "__main__":
    main()
