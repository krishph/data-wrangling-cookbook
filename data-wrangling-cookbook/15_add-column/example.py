import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["total"] = pdf["price"] * pdf["qty"]
print("pandas:\n", pdf)
