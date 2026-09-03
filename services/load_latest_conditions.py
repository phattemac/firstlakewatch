import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import sqlite3

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY

set_api_key(DATASTREAM_API_KEY)

from services.get_location import (
    get_location
)

location = get_location(
    "FIR_SD"
)

LOCATION_ID = location["datastream_id"]

MONITORING_LOCATION_ID = (
    location["monitoring_location_id"]
)

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

    characteristic = row.get(
        "CharacteristicName"
    )

    if characteristic not in wanted:
        continue

    date = row.get("ActivityStartDate")

    existing = latest.get(characteristic)

    if (
        existing is None
        or date > existing["sample_date"]
    ):
        latest[characteristic] = {
            "sample_date": date,
            "value": row.get("ResultValue"),
            "unit": row.get("ResultUnit")
        }

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

for characteristic, item in latest.items():

    cursor.execute(
        """
        INSERT OR REPLACE INTO
        latest_conditions
        (
            monitoring_location_id,
            characteristic_name,
            sample_date,
            value,
            unit
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            MONITORING_LOCATION_ID,
            characteristic,
            item["sample_date"],
            item["value"],
            item["unit"]
        )
    )

conn.commit()

print(
    f"Loaded {len(latest)} conditions."
)

conn.close()