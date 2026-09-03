import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

samples = [

    # Deep Basin
    (1, "2026-05-01", "pH", 8.1, "pH"),
    (1, "2026-06-01", "pH", 8.0, "pH"),
    (1, "2026-07-01", "pH", 7.8, "pH"),
    (1, "2026-08-24", "pH", 7.9, "pH"),

    # Beach Area
    (2, "2026-05-01", "pH", 8.2, "pH"),
    (2, "2026-06-01", "pH", 8.1, "pH"),
    (2, "2026-07-01", "pH", 8.0, "pH"),
    (2, "2026-08-20", "pH", 8.1, "pH"),

    # Sucker Brook
    (3, "2026-05-01", "pH", 7.4, "pH"),
    (3, "2026-06-01", "pH", 7.3, "pH"),
    (3, "2026-07-01", "pH", 7.3, "pH"),
    (3, "2026-08-15", "pH", 7.2, "pH")

]

cursor.executemany(
    """
    INSERT INTO samples (
        station_id,
        sample_date,
        parameter,
        value,
        unit
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    samples
)

conn.commit()

print("pH samples loaded.")

conn.close()