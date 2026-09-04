import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    latitude,
    longitude
FROM discovered_locations
WHERE monitoring_location_id IN
(
    'FLDS-1',
    'FLDS-2',
    'FLDS-3',
    'FIR_SD'
)
ORDER BY monitoring_location_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()