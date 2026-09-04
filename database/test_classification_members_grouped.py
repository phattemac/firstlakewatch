import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_classification_members_grouped import (
    get_classification_members_grouped
)

data = get_classification_members_grouped()

for classification, stations in data.items():

    print()
    print(classification)

    for station in stations:
        print(
            station[
                "monitoring_location_id"
            ]
        )