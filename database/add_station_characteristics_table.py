import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS station_characteristics (
    monitoring_location_id TEXT,
    location_name TEXT,
    characteristic_name TEXT,
    UNIQUE(
        monitoring_location_id,
        characteristic_name
    )
)
""")

conn.commit()

print("station_characteristics table created.")

conn.close()