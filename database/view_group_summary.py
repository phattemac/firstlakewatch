import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    group_name,
    station_count
FROM group_summary
ORDER BY group_name
""")

rows = cursor.fetchall()

print("Rows:", len(rows))
print()

for row in rows:
    print(row)

conn.close()