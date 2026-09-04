import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from services.get_featured_condition_dates import (
    get_featured_condition_dates
)

from services.get_featured_condition_age import (
    get_featured_condition_age
)

for row in get_featured_condition_dates():

    print(
        row["group_name"],
        "|",
        row["latest_date"],
        "|",
        get_featured_condition_age(
            row["latest_date"]
        ),
        "days old"
    )