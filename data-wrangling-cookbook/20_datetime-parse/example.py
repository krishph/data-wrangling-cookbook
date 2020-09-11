import pandas as pd

pdf  = pd.read_csv("data.csv", parse_dates=["ts"])
print("pandas dtypes:\n", pdf.dtypes)
