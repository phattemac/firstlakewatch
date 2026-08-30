import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT * FROM stations"
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()