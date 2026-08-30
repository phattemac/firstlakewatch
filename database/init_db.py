import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

# Stations

cursor.execute("""
CREATE TABLE IF NOT EXISTS stations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL,
    longitude REAL
)
""")

# Samples

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

# Updates

cursor.execute("""
CREATE TABLE IF NOT EXISTS updates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    update_date TEXT,
    source TEXT
)
""")

conn.commit()

print("Database initialized.")

conn.close()