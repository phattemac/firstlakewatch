import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY
from services.get_locations_in_group import (
    get_locations_in_group
)

set_api_key(DATASTREAM_API_KEY)

stations = get_locations_in_group(
    "ECOLI"
)

for station in stations:

    print()
    print("=" * 60)
    print(station["monitoring_location_id"])
    print("=" * 60)

    found = False

    results = observations(
        {
            "$filter":
            f"LocationId eq {station['datastream_id']}",
            "$top": 100
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

    for characteristic in sorted(characteristics):
        print(" -", characteristic)

        if "Escherichia coli" in characteristic:
            found = True

    print("E.COLI:", found)