import sqlite3


def get_group_locations(group_name):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sg.monitoring_location_id,
            dl.name,
            dl.datastream_id
        FROM station_groups sg
        LEFT JOIN discovered_locations dl
            ON sg.monitoring_location_id =
               dl.monitoring_location_id
        WHERE sg.group_name = ?
        ORDER BY sg.monitoring_location_id
        """,
        (group_name,)
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows