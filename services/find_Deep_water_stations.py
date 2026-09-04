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

    found_secchi = False

    results = observations(
        {
            "$filter": f"LocationId eq {location_id}",
            "$top": 500
        }
    )

    characteristics = set()

    for row in results:

        characteristic = row.get(
            "CharacteristicName"
        )

        if characteristic:

            characteristics.add(
                characteristic
            )

            if characteristic == "Depth, Secchi disk depth":
                found_secchi = True

    print("SECCHI:", found_secchi)
    print(
        "Parameter Count:",
        len(characteristics)
    )
