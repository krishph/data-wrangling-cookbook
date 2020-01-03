import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf.to_csv("out_pandas.csv", index=False)

print("wrote out_pandas.csv")
