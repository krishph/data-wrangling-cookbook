"""Split a compound field into columns — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    parts = df["location"].str.rsplit("-", n=1, expand=True)
    result = df.assign(city=parts[0], state=parts[1])
    print(result)
    return result


if __name__ == "__main__":
    main()
