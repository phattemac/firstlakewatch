import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

import sqlite3

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY

set_api_key(DATASTREAM_API_KEY)

PROFILE_STATIONS = {
    "FIR_SD": 907725,
    "FLDS-1": 201344,
    "FLDS-2": 201341,
    "FLDS-3": 201335
}

PROFILE_PARAMETERS = {
    "Dissolved oxygen (DO)",
    "Temperature, water",
    "pH",
    "Specific conductance"
}

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

loaded = 0

for station_id, datastream_id in PROFILE_STATIONS.items():

    print(
        f"Loading {station_id}..."
    )

    try:

        results = observations(
            {
                "$filter":
                f"LocationId eq {datastream_id}",
                "$top": 2000
            }
        )

        for row in results:

            characteristic = row.get(
                "CharacteristicName"
            )

            if characteristic not in PROFILE_PARAMETERS:
                continue

            depth = row.get(
                "ActivityDepthHeightMeasure"
            )

            if depth is None:
                continue

            try:
                depth = float(depth)
            except Exception:
                continue

            sample_date = row.get(
                "ActivityStartDate"
            )

            value = row.get(
                "ResultValue"
            )

            unit = row.get(
                "ResultUnit"
            )

            try:

                cursor.execute(
                    """
                    INSERT OR REPLACE INTO
                    profile_observations
                    (
                        monitoring_location_id,
                        sample_date,
                        depth,
                        characteristic_name,
                        value,
                        unit
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        station_id,
                        sample_date,
                        depth,
                        characteristic,
                        value,
                        unit
                    )
                )

                loaded += 1

            except Exception:
                pass

    except Exception as ex:

        print(
            f"ERROR loading {station_id}: {ex}"
        )

conn.commit()

print()
print(
    f"Loaded {loaded} profile observations."
)

conn.close()