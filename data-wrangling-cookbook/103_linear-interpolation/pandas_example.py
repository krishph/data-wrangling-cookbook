"""Interpolate gaps between observations: Estimate missing readings between known values in an evenly spaced time series."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    df = pd.read_csv(DATA_DIR / "data.csv").sort_values("minute")
    # Equal spacing makes row-based linear interpolation appropriate; do not extrapolate.
    result = df.assign(interpolated=df["temperature"].interpolate(method="linear", limit_area="inside"))
    print(result)
    return result


if __name__ == "__main__":
    main()
