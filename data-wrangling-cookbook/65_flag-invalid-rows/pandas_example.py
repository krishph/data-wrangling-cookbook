"""Flag records that violate data rules — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv")
    valid_age = df["age"].between(0, 120).fillna(False)
    valid_email = df["email"].str.contains(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", regex=True, na=False)
    result = df.assign(valid_age=valid_age, valid_email=valid_email, is_valid=valid_age & valid_email)
    print(result)
    return result


if __name__ == "__main__":
    main()
