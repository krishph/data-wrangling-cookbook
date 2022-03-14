import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas.query:\n", pdf.query("age > 28 and dept == 'eng'"))
