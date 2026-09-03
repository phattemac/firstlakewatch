import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    datastream_id,
    monitoring_location_id,
    name
FROM discovered_locations
ORDER BY name
""")

for row in cursor.fetchall():
    print(row)

conn.close()