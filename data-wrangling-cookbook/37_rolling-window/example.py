import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["ma3"] = pdf["sales"].rolling(window=3).mean()
print("pandas:\n", pdf)
