"""Select the top N rows per group: Keep the two best-selling products in each region with a deterministic tie-breaker."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    ordered = df.sort_values(["region", "revenue", "product"], ascending=[True, False, True])
    # Take exactly two rows per region; product name breaks revenue ties.
    result = ordered.groupby("region", sort=False).head(2).reset_index(drop=True)
    print(result)
    return result


if __name__ == "__main__":
    main()
