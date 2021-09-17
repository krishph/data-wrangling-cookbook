import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pd.get_dummies(pdf, columns=["color"]))
