"""Process a CSV with chunks or a lazy query — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    partials = []
    for chunk in pd.read_csv(DATA_DIR / "data.csv", usecols=["region", "quantity", "unit_price"], chunksize=2):
        chunk = chunk.loc[chunk["quantity"] >= 2].copy()
        chunk["revenue"] = chunk["quantity"] * chunk["unit_price"]
        partials.append(chunk.groupby("region", as_index=False)["revenue"].sum())
    result = pd.concat(partials, ignore_index=True).groupby("region", as_index=False)["revenue"].sum().sort_values("region")
    print(result)
    return result


if __name__ == "__main__":
    main()
