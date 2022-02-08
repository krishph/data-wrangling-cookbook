import pandas as pd

pdf = pd.read_csv("data.csv")
pdf["tags"] = pdf["tags"].str.split("|")
print("pandas:\n", pdf.explode("tags").reset_index(drop=True))
