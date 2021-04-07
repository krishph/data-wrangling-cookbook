import pandas as pd

a_pd = pd.read_csv("data.csv")
b_pd = pd.read_csv("data_b.csv")

print("pandas:\n", pd.concat([a_pd, b_pd], ignore_index=True))
