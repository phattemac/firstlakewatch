import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_classification_summary import (
    get_classification_summary
)

for row in get_classification_summary():
    print(row)