import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf.groupby("dept").agg(
    avg_sal=("salary", "mean"),
    max_sal=("salary", "max"),
    head_count=("employee", "count"),
).reset_index())
