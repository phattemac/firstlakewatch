import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_featured_condition_dates import (
    get_featured_condition_dates
)

for row in get_featured_condition_dates():
    print(row)