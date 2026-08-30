import sqlite3

DB_PATH = "database/firstlake.db"

def get_sample_history(station_id, parameter):

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sample_date,
            value
        FROM samples
        WHERE station_id = ?
        AND parameter = ?
        ORDER BY sample_date
        """,
        (station_id, parameter)
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows