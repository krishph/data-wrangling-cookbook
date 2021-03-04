import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pd.crosstab(pdf["dept"], pdf["level"]))
