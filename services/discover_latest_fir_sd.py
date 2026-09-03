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
        "$filter": "LocationId eq 907725",
        "$top": 20
    }
)

for row in results:

    print(
        row.get("ActivityStartDate"),
        "|",
        row.get("CharacteristicName"),
        "|",
        row.get("ResultValue"),
        "|",
        row.get("ResultUnit")
    )