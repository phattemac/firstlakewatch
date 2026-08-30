import sqlite3

DB_PATH = "database/firstlake.db"


def get_latest_ecoli(station_id):

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
        AND parameter = 'E.coli'
        ORDER BY sample_date DESC
        LIMIT 1
        """,
        (station_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)

    return None