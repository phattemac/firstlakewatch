import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_data_status import (
    get_data_status
)

for row in get_data_status():
    print(row)