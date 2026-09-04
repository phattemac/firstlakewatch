import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    group_name,
    characteristic_name,
    sample_date,
    value,
    unit
FROM featured_conditions
ORDER BY
    group_name,
    characteristic_name
""")

rows = cursor.fetchall()

print("Rows:", len(rows))
print()

for row in rows:
    print(row)

conn.close()