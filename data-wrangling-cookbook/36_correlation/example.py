import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf[["x", "y", "z"]].corr())
