import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf[pdf["age"] > 28])
