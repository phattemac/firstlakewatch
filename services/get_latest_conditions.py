import sqlite3

def get_latest_conditions(
    monitoring_location_id="FIR_SD"
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            characteristic_name,
            sample_date,
            value,
            unit
        FROM latest_conditions
        WHERE monitoring_location_id = ?
        ORDER BY characteristic_name
        """,
        (monitoring_location_id,)
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows