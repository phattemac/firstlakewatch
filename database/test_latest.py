import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.latest_samples import get_latest_ecoli

result = get_latest_ecoli(3)

print("RESULT:")
print(result)