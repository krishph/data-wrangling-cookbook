import pandas as pd

left_pd  = pd.read_csv("left.csv")
right_pd = pd.read_csv("right.csv")

print("pandas:\n", left_pd.merge(right_pd, on="id", how="outer"))
