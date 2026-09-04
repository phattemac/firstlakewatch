import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY

set_api_key(DATASTREAM_API_KEY)

results = observations(
    {
        "$filter": "LocationId eq 412847",
        "$top": 500
    }
)

characteristics = set()
depths = set()

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
        depths.add(depth)

print("Parameters:", len(characteristics))
print("Depths:", len(depths))
print()

for characteristic in sorted(characteristics):
    print(characteristic)

print()
print("Depths Found:")

for depth in sorted(depths):
    print(depth)