"""Compare each row with its group average — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(team_average=df.groupby("team")["score"].transform("mean"))
    result["difference"] = result["score"] - result["team_average"]
    print(result)
    return result


if __name__ == "__main__":
    main()
