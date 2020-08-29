import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["upper"]  = pdf["name"].str.upper()
pdf["length"] = pdf["name"].str.len()
print("pandas:\n", pdf)
