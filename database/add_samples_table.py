import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS samples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    station_id INTEGER,
    sample_date TEXT,
    parameter TEXT,
    value REAL,
    unit TEXT,
    FOREIGN KEY(station_id) REFERENCES stations(id)
)
""")

conn.commit()

print("Samples table created.")

conn.close()