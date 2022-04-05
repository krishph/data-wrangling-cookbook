import pandas as pd

pdf = pd.read_csv("data.csv", parse_dates=["ts"]).set_index("ts")
print("pandas weekly:\n", pdf.resample("W").sum())
