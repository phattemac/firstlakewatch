import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    sf.monitoring_location_id,
    sf.parameter_count,
    sf.depth_count,
    sf.has_ecoli,
    sf.has_secchi,
    sf.has_chlorophyll,
    sf.has_phosphorus
FROM station_fingerprints sf
JOIN station_classifications sc
    ON sf.monitoring_location_id =
       sc.monitoring_location_id
WHERE sc.classification =
      'UNCLASSIFIED'
ORDER BY sf.monitoring_location_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()