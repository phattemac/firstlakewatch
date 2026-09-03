import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS first_lake_locations (
    location_id TEXT PRIMARY KEY,
    location_name TEXT,
    latitude REAL,
    longitude REAL,
    source_dataset TEXT
)
""")

conn.commit()

print("first_lake_locations table created.")

conn.close()