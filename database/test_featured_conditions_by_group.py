import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_featured_conditions_by_group import (
    get_featured_conditions_by_group
)

for row in get_featured_conditions_by_group(
    "surface"
):
    print(row)