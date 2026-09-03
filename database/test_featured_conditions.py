import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_featured_conditions import (
    get_featured_conditions
)

print(
    get_featured_conditions()
)