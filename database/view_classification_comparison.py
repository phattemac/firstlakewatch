import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    sf.monitoring_location_id,

    sr.role,

    sc.classification,

    sf.parameter_count,
    sf.depth_count,
    sf.has_ecoli,
    sf.has_secchi,
    sf.has_chlorophyll,
    sf.has_phosphorus

FROM station_fingerprints sf

LEFT JOIN station_roles sr
    ON sf.monitoring_location_id =
       sr.monitoring_location_id

LEFT JOIN station_classifications sc
    ON sf.monitoring_location_id =
       sc.monitoring_location_id

ORDER BY sf.monitoring_location_id
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()