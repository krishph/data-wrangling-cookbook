"""Choose the first available value: Combine primary and backup contact columns by taking the first nonmissing value in each row."""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pl.read_csv(DATA_DIR / "data.csv")
    result = df.with_columns(pl.coalesce("primary_email", "backup_email").alias("contact_email"))
    print(result)
    return result


if __name__ == "__main__":
    main()
