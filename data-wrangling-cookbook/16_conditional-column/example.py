import numpy as np
import pandas as pd

pdf  = pd.read_csv("data.csv")

pdf["grade"] = np.where(pdf["score"] >= 70, "pass", "fail")
print("pandas:\n", pdf)
