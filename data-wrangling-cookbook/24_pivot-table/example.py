import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf.pivot_table(index="dept", columns="quarter",
                                    values="revenue", aggfunc="sum"))
