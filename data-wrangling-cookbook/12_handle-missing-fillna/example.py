import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf.fillna({"age": pdf["age"].mean()}))
