import pandas as pd

left_pd  = pd.read_csv("data.csv")
extra_pd = pd.read_csv("extra.csv")

print("pandas:\n", pd.concat([left_pd, extra_pd], axis=1))
