from services.get_featured_condition_dates import (
    get_featured_condition_dates
)

from services.get_featured_condition_age import (
    get_featured_condition_age
)


def get_data_status():

    results = []

    for row in get_featured_condition_dates():

        age = get_featured_condition_age(
            row["latest_date"]
        )

        if age <= 30:
            status = "CURRENT"

        elif age <= 365:
            status = "STALE"

        else:
            status = "HISTORICAL"

        results.append({
            "group_name": row["group_name"],
            "latest_date": row["latest_date"],
            "age_days": age,
            "status": status
        })

    return results