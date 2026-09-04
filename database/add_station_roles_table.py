import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS station_roles (
    monitoring_location_id TEXT PRIMARY KEY,
    role TEXT
)
""")

conn.commit()

print("station_roles table created.")

conn.close()