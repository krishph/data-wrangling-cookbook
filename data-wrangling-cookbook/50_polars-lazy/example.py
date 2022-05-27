import polars as pl

# scan_* returns a LazyFrame -- no I/O until .collect().
lf = (
    pl.scan_csv("data.csv")
      .filter(pl.col("salary") >= 90)
      .group_by("dept")
      .agg(pl.col("salary").mean().alias("avg_salary"))
      .sort("avg_salary", descending=True)
)
print("Query plan:\n", lf.explain())
print("Result:\n", lf.collect())
