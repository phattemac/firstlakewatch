import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS station_groups (
    monitoring_location_id TEXT PRIMARY KEY,
    group_name TEXT
)
""")

conn.commit()

print("station_groups table created.")

conn.close()