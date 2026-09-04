import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY

set_api_key(DATASTREAM_API_KEY)

stations = {
    "FLDS-1": 201344,
    "FLDS-2": 201341,
    "FLDS-3": 201335,
    "FIR_SD": 907725
}

for station_name, location_id in stations.items():

    print()
    print("=" * 60)
    print(station_name)
    print("=" * 60)

    values = []

    results = observations(
        {
            "$filter": f"LocationId eq {location_id}",
            "$top": 500
        }
    )

    for row in results:

        if row.get(
            "CharacteristicName"
        ) == "Depth, Secchi disk depth":

            value = row.get(
                "ResultValue"
            )

            if value is not None:
                values.append(float(value))

    if not values:

        print(
            "No Secchi measurements found."
        )

        continue

    values.sort()

    print("Samples:", len(values))
    print("Minimum:", min(values))
    print("Maximum:", max(values))
    print(
        "Average:",
        round(
            sum(values) / len(values),
            2
        )
    )

    print()
    print("Most Recent Values:")

    for value in values[-10:]:
        print(value)