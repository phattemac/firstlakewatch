import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    parameter_count,
    depth_count,
    has_ecoli,
    has_secchi,
    has_chlorophyll,
    has_phosphorus
FROM station_fingerprints
""")

stations = cursor.fetchall()

for (
    station,
    parameter_count,
    depth_count,
    has_ecoli,
    has_secchi,
    has_chlorophyll,
    has_phosphorus
) in stations:

    classification = "UNCLASSIFIED"
    reason = ""

    # Intensive profile stations
    if (
        depth_count >= 20
        and has_chlorophyll
        and has_phosphorus
    ):

        classification = (
            "INTENSIVE_PROFILE"
        )

        reason = (
            "Many depth samples plus "
            "chlorophyll and phosphorus"
        )

    # Standard profile stations
    elif (
        depth_count >= 5
        and has_secchi
    ):

        classification = (
            "PROFILE"
        )

        reason = (
            "Multiple depths and "
            "Secchi measurements"
        )

    # Rich chemistry stations
    elif (
        parameter_count >= 20
        and has_chlorophyll
    ):

        classification = (
            "CHEMISTRY"
        )

        reason = (
            "Rich chemistry suite "
            "with chlorophyll"
        )

    # Watershed chemistry stations
    elif parameter_count >= 20:

        classification = (
            "WATERSHED_CHEMISTRY"
        )

        reason = (
            "Large chemistry suite"
        )

        # Bacteria stations
    elif has_ecoli:

        classification = (
            "BACTERIA"
        )

        reason = (
            "Contains Escherichia coli"
        )

    # Basic field monitoring
    elif parameter_count >= 8:

        classification = (
            "FIELD_MONITORING"
        )

        reason = (
            "Core water quality "
            "parameters"
        )

    cursor.execute(
        """
        INSERT OR REPLACE INTO
        station_classifications
        (
            monitoring_location_id,
            classification,
            reason
        )
        VALUES (?, ?, ?)
        """,
        (
            station,
            classification,
            reason
        )
    )

conn.commit()

print(
    f"Classified {len(stations)} stations."
)

conn.close()