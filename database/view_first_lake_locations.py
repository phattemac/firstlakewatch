import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM first_lake_locations
ORDER BY location_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()