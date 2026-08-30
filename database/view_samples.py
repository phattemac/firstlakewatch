import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    station_id,
    sample_date,
    parameter,
    value
FROM samples
""")

for row in cursor.fetchall():
    print(row)

conn.close()