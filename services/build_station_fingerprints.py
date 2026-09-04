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
CREATE TABLE IF NOT EXISTS station_fingerprints (
    monitoring_location_id TEXT PRIMARY KEY,
    datastream_id INTEGER,
    location_name TEXT,
    parameter_count INTEGER,
    depth_count INTEGER,
    deepest_sample REAL,
    shallowest_sample REAL,
    has_ecoli INTEGER,
    has_secchi INTEGER,
    has_chlorophyll INTEGER,
    has_phosphorus INTEGER
)
""")

cursor.execute("""
SELECT
    monitoring_location_id,
    datastream_id,
    name
FROM discovered_locations
ORDER BY monitoring_location_id
""")

stations = cursor.fetchall()

for monitoring_location_id, datastream_id, name in stations:

    print()
    print(
        f"Processing {monitoring_location_id}"
    )

    characteristics = set()
    depths = set()

    has_ecoli = False
    has_secchi = False
    has_chlorophyll = False
    has_phosphorus = False

    try:

        results = observations(
            {
                "$filter":
                f"LocationId eq {datastream_id}",
                "$top": 500
            }
        )

        for row in results:

            characteristic = row.get(
                "CharacteristicName"
            )

            if characteristic:

                characteristics.add(
                    characteristic
                )

                if (
                    characteristic
                    == "Escherichia coli"
                ):
                    has_ecoli = True

                if (
                    characteristic
                    == "Depth, Secchi disk depth"
                ):
                    has_secchi = True

                if (
                    "Chlorophyll"
                    in characteristic
                ):
                    has_chlorophyll = True

                if (
                    "Phosphorus"
                    in characteristic
                ):
                    has_phosphorus = True

            depth = row.get(
                "ActivityDepthHeightMeasure"
            )

            if depth is not None:

                try:
                    depths.add(
                        float(depth)
                    )
                except Exception:
                    pass

    except Exception as ex:

        print(
            f"ERROR: {ex}"
        )

        continue

    parameter_count = len(
        characteristics
    )

    depth_count = len(
        depths
    )

    if depths:

        deepest_sample = min(depths)
        shallowest_sample = max(depths)

    else:

        deepest_sample = None
        shallowest_sample = None

    cursor.execute(
        """
        INSERT OR REPLACE INTO
        station_fingerprints
        (
            monitoring_location_id,
            datastream_id,
            location_name,
            parameter_count,
            depth_count,
            deepest_sample,
            shallowest_sample,
            has_ecoli,
            has_secchi,
            has_chlorophyll,
            has_phosphorus
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            monitoring_location_id,
            datastream_id,
            name,
            parameter_count,
            depth_count,
            deepest_sample,
            shallowest_sample,
            int(has_ecoli),
            int(has_secchi),
            int(has_chlorophyll),
            int(has_phosphorus)
        )
    )

conn.commit()

cursor.execute("""
SELECT COUNT(*)
FROM station_fingerprints
""")

count = cursor.fetchone()[0]

print()
print(
    f"Saved fingerprints for {count} stations."
)

conn.close()  