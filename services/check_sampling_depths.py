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

    depths = set()

    results = observations(
        {
            "$filter": f"LocationId eq {location_id}",
            "$top": 500
        }
    )

    for row in results:

        depth = row.get(
            "ActivityDepthHeightMeasure"
        )

        if depth is not None:
            depths.add(depth)

    if depths:

        print("Depths Found:")

        for depth in sorted(depths):
            print(depth)

    else:

        print(
            "No ActivityDepthHeightMeasure values found."
        )