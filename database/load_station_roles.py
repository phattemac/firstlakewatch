import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

roles = [

    # Intensive lake monitoring
    ("FLDS-1", "INTENSIVE_PROFILE"),
    ("FIR_SD", "INTENSIVE_PROFILE"),

    # Standard lake profiles
    ("FLDS-2", "PROFILE"),
    ("FLDS-3", "PROFILE"),

    # High-value chemistry stations
    ("FLOL-1", "CHEMISTRY"),
    ("119", "CHEMISTRY"),
    ("07-229", "CHEMISTRY"),
    ("FL", "CHEMISTRY"),

    # Watershed chemistry
    ("1STIN", "WATERSHED_CHEMISTRY"),
    ("1STOUT", "WATERSHED_CHEMISTRY"),

    # Bacteria stations
    ("FLEC-1", "BACTERIA"),
    ("FLEC-2", "BACTERIA"),
    ("FLEC-3A", "BACTERIA"),
    ("FLEC-3B", "BACTERIA"),
    ("FLEC-4A", "BACTERIA"),
    ("FLEC-4B", "BACTERIA"),
    ("FLEC-4C", "BACTERIA"),
    ("FLEC-5", "BACTERIA"),
    ("FLEC-5A", "BACTERIA"),
    ("FLEC-6", "BACTERIA"),
    ("FLEC-6A", "BACTERIA"),
    ("FLEC-7", "BACTERIA"),
    ("FLEC-7A", "BACTERIA"),
    ("FLEC-8", "BACTERIA"),

    # Tentatively bacteria until proven otherwise
    ("FLECD-1", "BACTERIA"),
    ("FLECD-2", "BACTERIA"),
    ("FLECD-3", "BACTERIA"),
    ("FLECD-4", "BACTERIA"),
    ("FLECD-5", "BACTERIA"),
]

cursor.executemany(
    """
    INSERT OR REPLACE INTO
    station_roles
    (
        monitoring_location_id,
        role
    )
    VALUES (?, ?)
    """,
    roles
)

conn.commit()

print(
    f"Loaded {len(roles)} station roles."
)

conn.close()