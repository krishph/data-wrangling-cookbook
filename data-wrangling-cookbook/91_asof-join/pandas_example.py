"""Match the most recent earlier observation — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    trades = pd.read_csv(DATA_DIR / "trades.csv", parse_dates=["time"]).sort_values("time")
    quotes = pd.read_csv(DATA_DIR / "quotes.csv", parse_dates=["time"]).sort_values("time")
    result = pd.merge_asof(trades, quotes, on="time", direction="backward", tolerance=pd.Timedelta("5s"))
    print(result)
    return result


if __name__ == "__main__":
    main()
