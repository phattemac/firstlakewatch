import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS discovered_parameters (
    monitoring_location_id TEXT,
    location_name TEXT,
    characteristic_name TEXT,
    UNIQUE (
        monitoring_location_id,
        characteristic_name
    )
)
""")

conn.commit()

conn.close()

print("Table created.")