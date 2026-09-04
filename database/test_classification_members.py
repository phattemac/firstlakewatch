import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_classification_members import (
    get_classification_members
)

for row in get_classification_members():
    print(row)