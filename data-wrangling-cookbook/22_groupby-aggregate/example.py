import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf.groupby("dept")["salary"].mean().reset_index())
