import glob
import pandas as pd

files = sorted(glob.glob("shards/*.csv"))

pdf = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
print("pandas:\n", pdf)
