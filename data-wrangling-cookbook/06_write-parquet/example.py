import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf.to_parquet("out_pandas.parquet")

print("wrote out_pandas.parquet")
