import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["rank"] = pdf["score"].rank(method="dense", ascending=False)
print("pandas:\n", pdf)
