import sqlite3


def get_station_group(
    monitoring_location_id
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT group_name
        FROM station_groups
        WHERE monitoring_location_id = ?
        """,
        (monitoring_location_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return row[0]

    return None