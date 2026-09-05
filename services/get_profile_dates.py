import sqlite3


def get_profile_dates(
    station_id
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT DISTINCT
            sample_date
        FROM profile_observations
        WHERE monitoring_location_id = ?
        ORDER BY sample_date
        """,
        (station_id,)
    )

    dates = [
        row[0]
        for row in cursor.fetchall()
    ]

    conn.close()

    return dates