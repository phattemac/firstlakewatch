import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_locations_in_group import (
    get_locations_in_group
)

for row in get_locations_in_group(
    "SURFACE"
):
    print(row)
