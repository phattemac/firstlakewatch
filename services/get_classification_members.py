import sqlite3


def get_classification_members():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sc.classification,
            sf.monitoring_location_id,
            sf.parameter_count,
            sf.depth_count
        FROM station_classifications sc
        JOIN station_fingerprints sf
            ON sc.monitoring_location_id =
               sf.monitoring_location_id
        ORDER BY
            sc.classification,
            sf.monitoring_location_id
        """
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows