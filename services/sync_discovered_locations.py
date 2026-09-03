import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import sqlite3

from datastream_py import (
    set_api_key,
    locations
)

from config.settings import DATASTREAM_API_KEY

set_api_key(DATASTREAM_API_KEY)

# Current approved monitoring zone
MIN_LAT = 44.7625
MAX_LAT = 44.7780

MIN_LON = -63.6760
MAX_LON = -63.6480

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS discovered_locations (
    id INTEGER PRIMARY KEY,
    datastream_id INTEGER,
    monitoring_location_id TEXT,
    name TEXT,
    latitude REAL,
    longitude REAL
)
""")

count = 0

results = locations(
    {
        "$select":
        "Id,ID,Name,Latitude,Longitude"
    }
)

for location in results:

    lat = location.get("Latitude")
    lon = location.get("Longitude")

    if lat is None or lon is None:
        continue

    if (
        MIN_LAT <= lat <= MAX_LAT
        and
        MIN_LON <= lon <= MAX_LON
    ):

        cursor.execute(
            """
            INSERT OR REPLACE INTO
            discovered_locations
            (
                datastream_id,
                monitoring_location_id,
                name,
                latitude,
                longitude
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                location["Id"],
                location["ID"],
                location["Name"],
                location["Latitude"],
                location["Longitude"]
            )
        )

        count += 1

conn.commit()

print(
    f"Saved {count} locations."
)

conn.close()
