import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["running"] = pdf["sales"].cumsum()
print("pandas:\n", pdf)
