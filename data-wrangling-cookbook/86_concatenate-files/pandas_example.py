"""Append files and retain source lineage — pandas implementation.

Run this file directly; input paths are relative to this file, not your terminal.
"""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "data"


def main():
    frames = []
    for name in ["january.csv", "february.csv"]:
        frame = pd.read_csv(DATA_DIR / name).assign(source_file=name)
        frames.append(frame)
    result = pd.concat(frames, ignore_index=True)
    print(result)
    return result


if __name__ == "__main__":
    main()
