import pandas as pd

pdf = pd.read_csv("data.csv", parse_dates=["ts"])
pdf["year"]    = pdf["ts"].dt.year
pdf["month"]   = pdf["ts"].dt.month
pdf["weekday"] = pdf["ts"].dt.day_name()
print("pandas:\n", pdf)
