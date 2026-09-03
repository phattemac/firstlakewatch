import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.get_locations_in_group import (
    get_locations_in_group
)

locations = get_locations_in_group(
    "SURFACE"
)

print("Surface Stations")
print()

for location in locations:

    print(
        location["monitoring_location_id"],
        "|",
        location["datastream_id"],
        "|",
        location["name"]
    )