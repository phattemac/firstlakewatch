import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS latest_conditions (
    monitoring_location_id TEXT,
    characteristic_name TEXT,
    sample_date TEXT,
    value REAL,
    unit TEXT,
    UNIQUE (
        monitoring_location_id,
        characteristic_name
    )
)
""")

conn.commit()

print("latest_conditions table created.")

conn.close()