import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY

set_api_key(DATASTREAM_API_KEY)

LOCATION_ID = 907725  # FIR_SD

wanted = {
    "pH",
    "Temperature, water",
    "Dissolved oxygen (DO)",
    "Specific conductance",
    "Total Phosphorus, mixed forms",
    "Chlorophyll a, corrected for pheophytin"
}

latest = {}

results = observations(
    {
        "$filter": f"LocationId eq {LOCATION_ID}",
        "$top": 5000
    }
)

for row in results:

    characteristic = row.get("CharacteristicName")

    if characteristic not in wanted:
        continue

    date = row.get("ActivityStartDate")

    existing = latest.get(characteristic)

    if (
        existing is None
        or date > existing["date"]
    ):
        latest[characteristic] = {
            "date": date,
            "value": row.get("ResultValue"),
            "unit": row.get("ResultUnit")
        }

for characteristic in sorted(latest):

    item = latest[characteristic]

    print(
        characteristic,
        "|",
        item["date"],
        "|",
        item["value"],
        "|",
        item["unit"]
    )