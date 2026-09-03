import sqlite3


def get_featured_station(group_name):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            fs.group_name,
            fs.monitoring_location_id,
            dl.name,
            dl.datastream_id
        FROM featured_stations fs
        JOIN discovered_locations dl
            ON fs.monitoring_location_id =
               dl.monitoring_location_id
        WHERE fs.group_name = ?
        """,
        (group_name,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)

    return None