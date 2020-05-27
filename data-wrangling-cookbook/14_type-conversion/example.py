import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["age"] = pdf["age"].astype("int32")
pdf["score"] = pdf["score"].astype("float32")
print("pandas dtypes:\n", pdf.dtypes)
