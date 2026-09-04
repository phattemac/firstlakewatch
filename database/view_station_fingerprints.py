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
    deepest_sample,
    has_ecoli,
    has_secchi,
    has_chlorophyll,
    has_phosphorus
FROM station_fingerprints
ORDER BY
    parameter_count DESC,
    depth_count DESC
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()