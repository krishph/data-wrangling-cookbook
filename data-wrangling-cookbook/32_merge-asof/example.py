import pandas as pd

quotes = pd.read_csv("data.csv", parse_dates=["ts"])
trades = pd.read_csv("trades.csv", parse_dates=["ts"])

# pandas -- both frames must be sorted on the "on" key.
out_pd = pd.merge_asof(trades.sort_values("ts"),
                       quotes.sort_values("ts"), on="ts")
print("pandas:\n", out_pd)
