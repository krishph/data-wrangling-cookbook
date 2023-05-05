"""Group by multiple dimensions — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.groupby(["region", "product"], as_index=False).agg(total_units=("quantity", "sum")).sort_values(["region", "product"])
    print(result)
    return result


if __name__ == "__main__":
    main()
