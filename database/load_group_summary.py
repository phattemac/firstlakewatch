import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM group_summary")

cursor.execute("""
SELECT
    group_name,
    COUNT(*)
FROM station_groups
GROUP BY group_name
""")

rows = cursor.fetchall()

cursor.executemany(
    """
    INSERT INTO
    group_summary
    (
        group_name,
        station_count
    )
    VALUES (?, ?)
    """,
    rows
)

conn.commit()

print(
    f"Loaded {len(rows)} summary rows."
)

conn.close()