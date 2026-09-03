import sqlite3


def get_locations_by_group(group_name):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            monitoring_location_id,
            group_name
        FROM station_groups
        WHERE group_name = ?
        ORDER BY monitoring_location_id
        """,
        (group_name,)
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows