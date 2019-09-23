import pandas as pd

# pandas -- needs openpyxl for .xlsx
# pdf = pd.read_excel("data.xlsx", sheet_name=0)

# Fallback so this script runs out-of-the-box:
pdf  = pd.read_csv("data.csv")
print("pandas:\n", pdf)
