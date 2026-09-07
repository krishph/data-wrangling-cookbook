"""Calculate monthly cohort retention: Group customers by first observed activity month and measure the share active in later months."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv", try_parse_dates=True)
    activity = df.select("customer_id", pl.col("activity_date").dt.truncate("1mo").alias("activity_month")).unique()
    cohorts = activity.group_by("customer_id").agg(pl.col("activity_month").min().alias("cohort_month"))
    sizes = cohorts.group_by("cohort_month").agg(pl.len().alias("cohort_size"))
    activity = activity.join(cohorts, on="customer_id", validate="m:1")
    activity = activity.with_columns(
        ((pl.col("activity_month").dt.year() - pl.col("cohort_month").dt.year()) * 12
         + pl.col("activity_month").dt.month().cast(pl.Int32)
         - pl.col("cohort_month").dt.month().cast(pl.Int32)).alias("month_number")
    )
    result = activity.group_by("cohort_month", "month_number").agg(pl.col("customer_id").n_unique().alias("active_customers"))
    result = result.join(sizes, on="cohort_month", validate="m:1").with_columns((100 * pl.col("active_customers") / pl.col("cohort_size")).alias("retention_percent")).sort("cohort_month", "month_number")
    # First observed activity is the cohort definition, not necessarily the true signup date.
    print(result)
    return result


if __name__ == "__main__":
    main()
