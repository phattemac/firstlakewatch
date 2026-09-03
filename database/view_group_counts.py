import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    group_name,
    COUNT(*)
FROM station_groups
GROUP BY group_name
ORDER BY group_name
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()