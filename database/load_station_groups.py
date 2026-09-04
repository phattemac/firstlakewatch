import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

groups = [

    ("FIR_SD", "DEEP_WATER"),

    ("FLDS-1", "DEEP_WATER"),
    ("FLDS-2", "SURFACE"),
    ("FLDS-3", "SURFACE"),

    ("FLEC-1", "ECOLI"),
    ("FLEC-2", "ECOLI"),
    ("FLEC-3A", "ECOLI"),
    ("FLEC-3B", "ECOLI"),
    ("FLEC-4A", "ECOLI"),
    ("FLEC-4B", "ECOLI"),
    ("FLEC-4C", "ECOLI"),
    ("FLEC-5", "ECOLI"),
    ("FLEC-5A", "ECOLI"),
    ("FLEC-6", "ECOLI"),
    ("FLEC-6A", "ECOLI"),
    ("FLEC-7", "ECOLI"),
    ("FLEC-7A", "ECOLI"),
    ("FLEC-8", "ECOLI"),

    ("FLECD-1", "DITCH"),
    ("FLECD-2", "DITCH"),
    ("FLECD-3", "DITCH"),
    ("FLECD-4", "DITCH"),
    ("FLECD-5", "DITCH"),

    ("FIR_OUT", "OUTFLOW"),
    ("1STOUT", "OUTFLOW"),

    ("1STIN", "INFLOW"),

    ("FLOL-1", "LAKE")
]

cursor.executemany(
    """
    INSERT OR REPLACE INTO
    station_groups
    (
        monitoring_location_id,
        group_name
    )
    VALUES (?, ?)
    """,
    groups
)

conn.commit()

print(
    f"Loaded {len(groups)} station groups."
)

conn.close()