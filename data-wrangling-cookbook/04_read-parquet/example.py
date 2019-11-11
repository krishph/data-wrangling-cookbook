import pandas as pd

# Round-trip CSV -> Parquet -> DataFrame so the recipe is self-contained.
pd.read_csv("data.csv").to_parquet("data.parquet")

pdf  = pd.read_parquet("data.parquet")
print("pandas:\n", pdf)
