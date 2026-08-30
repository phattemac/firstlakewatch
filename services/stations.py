import sqlite3

DB_PATH = "database/firstlake.db"

def get_stations():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM stations
        ORDER BY name
        """
    )

    stations = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return stations