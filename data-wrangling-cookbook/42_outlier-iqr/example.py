import pandas as pd

pdf  = pd.read_csv("data.csv")

q1, q3 = pdf["value"].quantile([0.25, 0.75])
iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
pdf["is_outlier"] = (pdf["value"] < lo) | (pdf["value"] > hi)
print("pandas:\n", pdf)
