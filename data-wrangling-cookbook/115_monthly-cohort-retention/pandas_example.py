"""Calculate monthly cohort retention: Group customers by first observed activity month and measure the share active in later months."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv", parse_dates=["activity_date"])
    df["activity_month"] = df["activity_date"].dt.to_period("M").dt.to_timestamp()
    # Deduplicate repeat activity before counting active customers.
    activity = df[["customer_id", "activity_month"]].drop_duplicates().copy()
    cohorts = activity.groupby("customer_id", as_index=False).agg(cohort_month=("activity_month", "min"))
    sizes = cohorts.groupby("cohort_month", as_index=False).agg(cohort_size=("customer_id", "size"))
    activity = activity.merge(cohorts, on="customer_id", validate="many_to_one")
    activity["month_number"] = (activity["activity_month"].dt.year - activity["cohort_month"].dt.year) * 12 + activity["activity_month"].dt.month - activity["cohort_month"].dt.month
    result = activity.groupby(["cohort_month", "month_number"], as_index=False).agg(active_customers=("customer_id", "nunique"))
    result = result.merge(sizes, on="cohort_month", validate="many_to_one")
    result["retention_percent"] = 100 * result["active_customers"] / result["cohort_size"]
    # Only observed cohort/month pairs appear; missing history is not automatically zero retention.
    result = result.sort_values(["cohort_month", "month_number"])
    print(result)
    return result


if __name__ == "__main__":
    main()
