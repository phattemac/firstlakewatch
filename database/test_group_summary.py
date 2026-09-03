import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_group_summary import (
    get_group_summary
)

for row in get_group_summary():
    print(row)