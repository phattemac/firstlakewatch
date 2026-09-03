import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_latest_conditions import (
    get_latest_conditions
)

for row in get_latest_conditions():

    print(row)