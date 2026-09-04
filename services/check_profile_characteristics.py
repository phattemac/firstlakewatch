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
    "FIR_SD": 907725,
    "1STIN": 935453,
    "1STOUT": 935458
}

for station_name, location_id in stations.items():

    print()
    print("=" * 70)
    print(station_name)
    print("=" * 70)

    characteristics = set()
    depths = set()

    results = observations(
        {
            "$filter": f"LocationId eq {location_id}",
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

    print(
        "Parameter Count:",
        len(characteristics)
    )

    print(
        "Depth Count:",
        len(depths)
    )

    print(
        "Contains E.coli:",
        "Escherichia coli" in characteristics
    )

    print(
        "Contains Chlorophyll:",
        any(
            "Chlorophyll" in c
            for c in characteristics
        )
    )

    print(
        "Contains Phosphorus:",
        any(
            "Phosphorus" in c
            for c in characteristics
        )
    )

    print(
        "Contains Secchi:",
        "Depth, Secchi disk depth"
        in characteristics
    )

    print()

    print("Characteristic List:")

    for characteristic in sorted(characteristics):
        print(" -", characteristic)