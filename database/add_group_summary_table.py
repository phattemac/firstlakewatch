import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS group_summary (
    group_name TEXT PRIMARY KEY,
    station_count INTEGER
)
""")

conn.commit()

print("group_summary table created.")

conn.close()