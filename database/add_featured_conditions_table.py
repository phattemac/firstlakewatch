import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS featured_conditions (
    group_name TEXT,
    characteristic_name TEXT,
    sample_date TEXT,
    value REAL,
    unit TEXT,
    UNIQUE(
        group_name,
        characteristic_name
    )
)
""")

conn.commit()

print("featured_conditions table created.")

conn.close()