import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    sample_date,
    depth,
    characteristic_name,
    value,
    unit
FROM profile_observations
ORDER BY sample_date DESC
LIMIT 50
""")

rows = cursor.fetchall()

print(
    f"Rows Returned: {len(rows)}"
)

print()

for row in rows:
    print(row)

conn.close()