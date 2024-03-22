"""Append files and retain source lineage — polars implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import polars as pl

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    frames = []
    for name in ["january.csv", "february.csv"]:
        frame = pl.read_csv(DATA_DIR / name).with_columns(pl.lit(name).alias("source_file"))
        frames.append(frame)
    result = pl.concat(frames, how="vertical")
    print(result)
    return result


if __name__ == "__main__":
    main()
