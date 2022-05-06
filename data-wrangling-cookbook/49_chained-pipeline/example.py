import pandas as pd

pdf  = pd.read_csv("data.csv")

out_pd = (
    pdf
    .query("salary >= 80")
    .assign(bonus=lambda d: d["salary"] * 0.1)
    .groupby("dept", as_index=False)
    .agg(total_bonus=("bonus", "sum"))
    .sort_values("total_bonus", ascending=False)
)
print("pandas:\n", out_pd)
