import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["domain"] = pdf["email"].str.extract(r"@(.+)$")
print("pandas:\n", pdf)
