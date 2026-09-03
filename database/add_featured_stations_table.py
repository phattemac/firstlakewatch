import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS featured_stations (
    group_name TEXT PRIMARY KEY,
    monitoring_location_id TEXT
)
""")

conn.commit()

print("featured_stations table created.")

conn.close()