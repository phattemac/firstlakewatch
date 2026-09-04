import sqlite3


def get_featured_condition_dates():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        group_name,
        MAX(sample_date) AS latest_date
    FROM featured_conditions
    GROUP BY group_name
    ORDER BY group_name
    """)

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows