import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_stations_by_classification import (
    get_stations_by_classification
)

for row in get_stations_by_classification(
    "INTENSIVE_PROFILE"
):
    print(row)