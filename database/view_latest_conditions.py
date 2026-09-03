import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    characteristic_name,
    sample_date,
    value,
    unit
FROM latest_conditions
ORDER BY characteristic_name
""")

rows = cursor.fetchall()

print("Rows:", len(rows))
print()

for row in rows:
    print(row)

conn.close()