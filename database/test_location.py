import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_location import (
    get_location
)

print(
    get_location("FIR_SD")
)