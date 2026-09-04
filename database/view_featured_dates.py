import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    group_name,
    MAX(sample_date)
FROM featured_conditions
GROUP BY group_name
ORDER BY group_name
""")

for row in cursor.fetchall():
    print(row)

conn.close()