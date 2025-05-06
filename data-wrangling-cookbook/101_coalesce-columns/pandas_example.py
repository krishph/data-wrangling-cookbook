"""Choose the first available value: Combine primary and backup contact columns by taking the first nonmissing value in each row."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    result = df.assign(contact_email=df["primary_email"].combine_first(df["backup_email"]))
    print(result)
    return result


if __name__ == "__main__":
    main()
