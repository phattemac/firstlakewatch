import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS profile_observations (
    monitoring_location_id TEXT,
    sample_date TEXT,
    depth REAL,
    characteristic_name TEXT,
    value REAL,
    unit TEXT,

    PRIMARY KEY (
        monitoring_location_id,
        sample_date,
        depth,
        characteristic_name
    )
)
""")

conn.commit()

print(
    "profile_observations table created."
)

conn.close()