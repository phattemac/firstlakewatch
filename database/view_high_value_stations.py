import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    parameter_count,
    depth_count,
    has_ecoli,
    has_secchi,
    has_chlorophyll,
    has_phosphorus
FROM station_fingerprints
WHERE parameter_count >= 20
ORDER BY parameter_count DESC
""")

for row in cursor.fetchall():
    print(row)

conn.close()