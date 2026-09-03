import sqlite3

DB_PATH = "database/firstlake.db"


def get_latest_parameter(station_id, parameter):

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sample_date,
            value,
            parameter
        FROM samples
        WHERE station_id = ?
        AND parameter = ?
        ORDER BY sample_date DESC
        LIMIT 1
        """,
        (station_id, parameter)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)

    return None


if __name__ == "__main__":

    print("Station 1 pH:")
    print(get_latest_parameter(1, "pH"))

  