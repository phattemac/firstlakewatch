import sqlite3


def get_featured_conditions_by_group(
    group_name
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
        FROM featured_conditions
        WHERE group_name = ?
        ORDER BY characteristic_name
        """,
        (group_name,)
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows
