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
    monitoring_location_id,
    datastream_id,
    name
FROM discovered_locations
ORDER BY monitoring_location_id
""")

stations = cursor.fetchall()

conn.close()

summary = []

for monitoring_location_id, datastream_id, name in stations:

    print()
    print("=" * 70)
    print(
        monitoring_location_id,
        "|",
        name
    )
    print("=" * 70)

    depths = set()

    try:

        results = observations(
            {
                "$filter":
                f"LocationId eq {datastream_id}",
                "$top": 500
            }
        )

        for row in results:

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

        print("ERROR:", ex)
        continue

    if not depths:

        print(
            "No depth measurements"
        )

        summary.append(
            (
                monitoring_location_id,
                0,
                None,
                None
            )
        )

        continue

    depth_list = sorted(depths)

    depth_count = len(depth_list)

    shallowest = max(depth_list)
    deepest = min(depth_list)

    print(
        "Depth Count:",
        depth_count
    )

    print(
        "Shallowest:",
        shallowest
    )

    print(
        "Deepest:",
        deepest
    )

    print()
    print("Depths:")

    for depth in depth_list:
        print(depth)

    summary.append(
        (
            monitoring_location_id,
            depth_count,
            shallowest,
            deepest
        )
    )

print()
print()
print("=" * 70)
print("SUMMARY")
print("=" * 70)

summary.sort(
    key=lambda x: x[1],
    reverse=True
)

for station_id, count, shallowest, deepest in summary:

    print(
        station_id,
        "| depths:",
        count,
        "| shallowest:",
        shallowest,
        "| deepest:",
        deepest
    )