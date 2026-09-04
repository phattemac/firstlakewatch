import sqlite3


def get_classification_summary():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            classification,
            COUNT(*) AS station_count
        FROM station_classifications
        GROUP BY classification
        ORDER BY classification
        """
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows


if __name__ == "__main__":

    for row in get_classification_summary():

        print(
            f"{row['classification']}: "
            f"{row['station_count']}"
        )