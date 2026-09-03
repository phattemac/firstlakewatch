import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_station_group import (
    get_station_group
)

print(get_station_group("FIR_SD"))
print(get_station_group("FLEC-1"))
print(get_station_group("FLECD-1"))
print(get_station_group("1STIN"))