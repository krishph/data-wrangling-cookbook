import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["rn"] = (pdf.sort_values(["dept", "salary"], ascending=[True, False])
                .groupby("dept").cumcount() + 1)
print("pandas:\n", pdf.sort_values(["dept", "rn"]))
