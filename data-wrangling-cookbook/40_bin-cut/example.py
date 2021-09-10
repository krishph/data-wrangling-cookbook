import pandas as pd

pdf  = pd.read_csv("data.csv")

bins   = [0, 18, 40, 65, 120]
labels = ["minor", "young", "adult", "senior"]
pdf["group"] = pd.cut(pdf["age"], bins=bins, labels=labels, right=False)
print("pandas:\n", pdf)
