import sqlite3

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    role,
    monitoring_location_id
FROM station_roles
ORDER BY
    role,
    monitoring_location_id
""")

current_role = None

for role, station in cursor.fetchall():

    if role != current_role:

        current_role = role

        print()
        print("=" * 60)
        print(role)
        print("=" * 60)

    print(station)

conn.close()