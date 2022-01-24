import pandas as pd

pdf  = pd.read_csv("data.csv")

print("pandas:\n", pdf.sample(n=3, random_state=42))
