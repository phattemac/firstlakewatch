import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_group_locations import (
    get_group_locations
)

for row in get_group_locations(
    "DEEP_WATER"
):
    print(row)