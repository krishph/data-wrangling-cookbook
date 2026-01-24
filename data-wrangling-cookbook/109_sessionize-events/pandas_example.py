"""Assign sessions to user events: Start a new session whenever a user’s consecutive events are more than 30 minutes apart."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["timestamp"]).sort_values(["user_id", "timestamp", "event_id"])
    gap = df.groupby("user_id")["timestamp"].diff()
    df["new_session"] = gap.isna() | (gap > pd.Timedelta(minutes=30))
    # Session numbers restart per user; exactly 30 minutes stays in the same session.
    result = df.assign(session_id=df.groupby("user_id")["new_session"].cumsum()).drop(columns="new_session")
    print(result)
    return result


if __name__ == "__main__":
    main()
