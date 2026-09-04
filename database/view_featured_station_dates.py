import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    group_name,
    characteristic_name,
    sample_date
FROM featured_conditions
ORDER BY
    group_name,
    sample_date DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()