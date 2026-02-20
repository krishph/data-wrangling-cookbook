"""Count consecutive value streaks: Number runs of repeated statuses and count each row’s position within its run."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv").sort_values("day")
    # This sample is one entity with complete statuses and one observation per day.
    new_run = df["status"].ne(df["status"].shift()).fillna(True)
    df["run_id"] = new_run.astype("int64").cumsum()
    result = df.assign(streak_length=df.groupby("run_id").cumcount() + 1)
    print(result)
    return result


if __name__ == "__main__":
    main()
