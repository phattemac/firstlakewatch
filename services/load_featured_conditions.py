import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import sqlite3

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY
from services.get_featured_conditions import (
    get_featured_conditions
)

set_api_key(DATASTREAM_API_KEY)

featured = get_featured_conditions()

wanted = {
    "pH",
    "Temperature, water",
    "Dissolved oxygen (DO)",
    "Specific conductance",
    "Total Phosphorus, mixed forms",
    "Chlorophyll a, corrected for pheophytin"
}

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

for group_name, station in featured.items():

    datastream_id = station["datastream_id"]

    latest = {}

    results = observations(
        {
            "$filter": f"LocationId eq {datastream_id}",
            "$top": 1000
        }
    )

    for row in results:

        characteristic = row.get(
            "CharacteristicName"
        )

        if characteristic not in wanted:
            continue

        date = row.get(
            "ActivityStartDate"
        )

        existing = latest.get(
            characteristic
        )

        if (
            existing is None
            or date > existing["sample_date"]
        ):
            latest[characteristic] = {
                "sample_date": date,
                "value": row.get("ResultValue"),
                "unit": row.get("ResultUnit")
            }

    for characteristic, item in latest.items():

        cursor.execute(
            """
            INSERT OR REPLACE INTO
            featured_conditions
            (
                group_name,
                characteristic_name,
                sample_date,
                value,
                unit
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                group_name,
                characteristic,
                item["sample_date"],
                item["value"],
                item["unit"]
            )
        )

conn.commit()

print("Featured conditions loaded.")

conn.close()