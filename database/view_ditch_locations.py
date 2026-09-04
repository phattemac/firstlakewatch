import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    name,
    latitude,
    longitude
FROM discovered_locations
WHERE monitoring_location_id IN
(
    'FLECD-1',
    'FLECD-2',
    'FLECD-3',
    'FLECD-4',
    'FLECD-5'
)
ORDER BY monitoring_location_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()