import sqlite3


def get_network_statistics():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    cursor = conn.cursor()

    # Total stations
    cursor.execute("""
    SELECT COUNT(*)
    FROM station_fingerprints
    """)

    total_stations = cursor.fetchone()[0]

    # Total classifications
    cursor.execute("""
    SELECT COUNT(DISTINCT classification)
    FROM station_classifications
    """)

    total_classifications = cursor.fetchone()[0]

    # Bacteria stations
    cursor.execute("""
    SELECT COUNT(*)
    FROM station_classifications
    WHERE classification = 'BACTERIA'
    """)

    bacteria_stations = cursor.fetchone()[0]

    # Profile stations
    cursor.execute("""
    SELECT COUNT(*)
    FROM station_classifications
    WHERE classification IN
    (
        'PROFILE',
        'INTENSIVE_PROFILE'
    )
    """)

    profile_stations = cursor.fetchone()[0]

    # Maximum parameter count
    cursor.execute("""
    SELECT MAX(parameter_count)
    FROM station_fingerprints
    """)

    max_parameters = cursor.fetchone()[0]

    # Maximum depth count
    cursor.execute("""
    SELECT MAX(depth_count)
    FROM station_fingerprints
    """)

    max_depth_levels = cursor.fetchone()[0]

    # Deepest sample
    cursor.execute("""
    SELECT MIN(deepest_sample)
    FROM station_fingerprints
    WHERE deepest_sample IS NOT NULL
    """)

    deepest_sample = cursor.fetchone()[0]

    conn.close()

    return {
        "total_stations": total_stations,
        "total_classifications": total_classifications,
        "bacteria_stations": bacteria_stations,
        "profile_stations": profile_stations,
        "max_parameters": max_parameters,
        "max_depth_levels": max_depth_levels,
        "deepest_sample": deepest_sample
    }


if __name__ == "__main__":

    stats = get_network_statistics()

    for key, value in stats.items():
        print(f"{key}: {value}")