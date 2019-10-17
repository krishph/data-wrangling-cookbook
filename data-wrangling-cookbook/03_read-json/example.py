import json, pathlib
import pandas as pd

# Generate a records JSON alongside the CSV for the demo.
records = [
    {"id": 1, "event": "click", "ts": "2026-01-01"},
    {"id": 2, "event": "view",  "ts": "2026-01-02"},
]
pathlib.Path("data.json").write_text(json.dumps(records))

pdf  = pd.read_json("data.json")
print("pandas:\n", pdf)
