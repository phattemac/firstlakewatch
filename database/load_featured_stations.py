import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

featured = [
    ("DEEP_WATER", "FIR_SD"),
    ("SURFACE", "FLDS-1"),
    ("ECOLI", "FLEC-1"),
    ("DITCH", "FLECD-1"),
    ("INFLOW", "1STIN"),
    ("OUTFLOW", "1STOUT"),
    ("LAKE", "FLOL-1")
]

cursor.executemany(
    """
    INSERT OR REPLACE INTO
    featured_stations
    (
        group_name,
        monitoring_location_id
    )
    VALUES (?, ?)
    """,
    featured
)

conn.commit()

print(
    f"Loaded {len(featured)} featured stations."
)

conn.close()