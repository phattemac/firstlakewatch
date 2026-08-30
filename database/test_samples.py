import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.samples import get_sample_history

rows = get_sample_history(
    3,
    "E.coli"
)

for row in rows:
    print(row)