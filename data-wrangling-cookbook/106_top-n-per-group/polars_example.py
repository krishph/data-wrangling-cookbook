"""Select the top N rows per group: Keep the two best-selling products in each region with a deterministic tie-breaker."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    ordered = df.sort(["region", "revenue", "product"], descending=[False, True, False])
    result = ordered.group_by("region", maintain_order=True).head(2).sort(["region", "revenue", "product"], descending=[False, True, False])
    print(result)
    return result


if __name__ == "__main__":
    main()
