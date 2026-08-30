import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

stations = [
    ("Deep Basin", 44.7725, -63.6685),
    ("Beach Area", 44.7739, -63.6710),
    ("Sucker Brook", 44.7692, -63.6595)
]

cursor.executemany(
    """
    INSERT INTO stations (
        name,
        latitude,
        longitude
    )
    VALUES (?, ?, ?)
    """,
    stations
)

conn.commit()

print("Stations added.")

conn.close()