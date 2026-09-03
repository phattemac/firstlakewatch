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

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    datastream_id,
    monitoring_location_id,
    name
FROM discovered_locations
ORDER BY name
""")

locations = cursor.fetchall()

conn.close()

for datastream_id, monitoring_location_id, name in locations:

    print()
    print("=" * 60)
    print(monitoring_location_id, "-", name)
    print("=" * 60)

    characteristics = set()
    record_count = 0

    try:

        results = observations(
            {
                "$filter": f"LocationId eq {datastream_id}",
                "$top": 1000
            }
        )

        for row in results:

            record_count += 1

            characteristic = row.get(
                "CharacteristicName"
            )

            if characteristic:
                characteristics.add(
                    characteristic
                )

    except Exception as ex:

        print("ERROR:", ex)
        continue

    print("Records found:", record_count)

    db = sqlite3.connect(
        "database/firstlake.db"
    )

    db_cursor = db.cursor()

    for characteristic in sorted(characteristics):

        print(" -", characteristic)

        db_cursor.execute(
            """
            INSERT OR IGNORE INTO
            station_characteristics
            (
                monitoring_location_id,
                location_name,
                characteristic_name
            )
            VALUES (?, ?, ?)
            """,
            (
                monitoring_location_id,
                name,
                characteristic
            )
        )

    db.commit()
    db.close()