import sqlite3


def get_stations_by_classification(
    classification
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sf.monitoring_location_id,
            sf.parameter_count,
            sf.depth_count
        FROM station_fingerprints sf
        JOIN station_classifications sc
            ON sf.monitoring_location_id =
               sc.monitoring_location_id
        WHERE sc.classification = ?
        ORDER BY sf.monitoring_location_id
        """,
        (classification,)
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows