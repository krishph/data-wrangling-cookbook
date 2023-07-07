"""Build a frequency and percentage table — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.groupby("priority", dropna=False).size().reset_index(name="count")
    result["percent"] = (100 * result["count"] / result["count"].sum()).round(2)
    result = result.sort_values(["count", "priority"], ascending=[False, True])
    print(result)
    return result


if __name__ == "__main__":
    main()
