"""Calculate elapsed time and flag overdue work: Measure ticket resolution time in hours and flag completed tickets exceeding a 24-hour target."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["opened_at", "closed_at"])
    # Timestamps share a timezone; the target uses elapsed hours, not business hours.
    hours = (df["closed_at"] - df["opened_at"]).dt.total_seconds() / 3600
    result = df.assign(resolution_hours=hours)
    # Open tickets have an unknown breach status until a reporting cutoff is supplied.
    result["breached"] = hours.gt(24).astype("boolean").mask(hours.isna(), pd.NA)
    print(result)
    return result


if __name__ == "__main__":
    main()
