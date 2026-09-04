import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS station_classifications (
    monitoring_location_id TEXT PRIMARY KEY,
    classification TEXT,
    reason TEXT
)
""")

conn.commit()

print("station_classifications table created.")

conn.close()