import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute(
    """
    SELECT
        monitoring_location_id,
        sample_date,
        depth,
        characteristic_name,
        value,
        unit
    FROM profile_observations
    WHERE monitoring_location_id = ?
    AND characteristic_name = ?
    ORDER BY
        sample_date DESC,
        depth
    """,
    (
        "FIR_SD",
        "Dissolved oxygen (DO)"
    )
)

rows = cursor.fetchall()

print(
    f"Rows: {len(rows)}"
)

print()

for row in rows[:100]:

    print(row)

print()

dates = sorted(
    list(
        set(
            row[1]
            for row in rows
        )
    ),
    reverse=True
)

print(
    "Unique Dates:",
    len(dates)
)

print()

for date in dates:

    count = sum(
        1
        for row in rows
        if row[1] == date
    )

    print(
        date,
        "|",
        count,
        "records"
    )

conn.close()