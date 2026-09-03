import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    group_name
FROM station_groups
ORDER BY group_name,
         monitoring_location_id
""")

rows = cursor.fetchall()

print("Rows:", len(rows))
print()

for row in rows:
    print(row)

conn.close()