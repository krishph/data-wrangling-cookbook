"""Unpivot wide data into tidy rows — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.melt(id_vars="store", value_vars=["Jan", "Feb", "Mar"], var_name="month", value_name="sales").sort_values(["store", "month"])
    print(result)
    return result


if __name__ == "__main__":
    main()
