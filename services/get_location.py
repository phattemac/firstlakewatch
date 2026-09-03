import sqlite3


def get_location(
    monitoring_location_id
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            monitoring_location_id,
            name,
            datastream_id
        FROM discovered_locations
        WHERE monitoring_location_id = ?
        """,
        (monitoring_location_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)

    return None