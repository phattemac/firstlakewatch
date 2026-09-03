import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_featured_station import (
    get_featured_station
)

print(
    get_featured_station("DEEP_WATER")
)

print(
    get_featured_station("SURFACE")
)