import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["bucket"] = pdf["score"].apply(lambda s: "hi" if s >= 90 else "lo")
print("pandas:\n", pdf)
