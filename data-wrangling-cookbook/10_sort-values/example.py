import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf.sort_values("score", ascending=False))
