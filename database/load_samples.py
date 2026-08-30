import sqlite3

conn = sqlite3.connect("database/firstlake.db")

cursor = conn.cursor()

samples = [

    # Deep Basin
    (1, "2026-05-01", "E.coli", 2, "CFU/100mL"),
    (1, "2026-06-01", "E.coli", 3, "CFU/100mL"),
    (1, "2026-07-01", "E.coli", 5, "CFU/100mL"),
    (1, "2026-08-24", "E.coli", 4, "CFU/100mL"),

    # Beach Area
    (2, "2026-05-01", "E.coli", 10, "CFU/100mL"),
    (2, "2026-06-01", "E.coli", 15, "CFU/100mL"),
    (2, "2026-07-01", "E.coli", 20, "CFU/100mL"),
    (2, "2026-08-20", "E.coli", 18, "CFU/100mL"),

    # Sucker Brook
    (3, "2026-05-01", "E.coli", 40, "CFU/100mL"),
    (3, "2026-06-01", "E.coli", 60, "CFU/100mL"),
    (3, "2026-07-01", "E.coli", 90, "CFU/100mL"),
    (3, "2026-08-15", "E.coli", 125, "CFU/100mL")
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

print("Sample data loaded.")

conn.close()