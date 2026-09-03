import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from datastream_py import (
    set_api_key,
    observations
)

from config.settings import DATASTREAM_API_KEY

set_api_key(DATASTREAM_API_KEY)

LOCATION_ID = 201344  # FLDS-1

results = observations(
    {
        "$filter": f"LocationId eq {LOCATION_ID}",
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

print("FLDS-1 Characteristics")
print()

for characteristic in sorted(characteristics):
    print(characteristic)