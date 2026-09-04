from datetime import datetime


def get_featured_condition_age(
    latest_date
):

    sample_date = datetime.strptime(
        latest_date,
        "%Y-%m-%d"
    )

    return (
        datetime.now()
        - sample_date
    ).days