import sqlite3


def get_group_summary():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        group_name,
        station_count
    FROM group_summary
    ORDER BY group_name
    """)

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows