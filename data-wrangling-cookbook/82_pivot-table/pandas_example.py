"""Pivot long data into a summary table — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.pivot_table(index="region", columns="product", values="quantity", aggfunc="sum", fill_value=0).reset_index()
    result.columns.name = None
    result = result[["region", "Book", "Folder", "Pen"]].sort_values("region")
    print(result)
    return result


if __name__ == "__main__":
    main()
