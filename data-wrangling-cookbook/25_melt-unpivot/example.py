import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf.melt(id_vars="dept", var_name="quarter",
                             value_name="revenue"))
