import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    role,
    COUNT(*)
FROM station_roles
GROUP BY role
ORDER BY role
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()