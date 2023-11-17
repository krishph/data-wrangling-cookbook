"""Convert UTC timestamps to local time — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(utc_time=pd.to_datetime(df["timestamp"], utc=True))
    result["new_york_time"] = result["utc_time"].dt.tz_convert("America/New_York")
    print(result)
    return result


if __name__ == "__main__":
    main()
