import sqlite3
import pandas as pd

print("Loading CSV...")

df = pd.read_csv(
    "database/first_lake_locations.csv"
)

print("Rows found:", len(df))

print("Columns:")
for col in df.columns:
    print(col)

conn = sqlite3.connect("database/firstlake.db")

rows = []

for _, row in df.iterrows():

    rows.append((
        row["MonitoringLocationID"],
        row["MonitoringLocationName"],
        row["MonitoringLocationLatitude"],
        row["MonitoringLocationLongitude"],
        "Friends of First Lake"
    ))

print("Rows prepared:", len(rows))

conn.executemany(
    """
    INSERT OR REPLACE INTO
    first_lake_locations
    (
        location_id,
        location_name,
        latitude,
        longitude,
        source_dataset
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    rows
)

conn.commit()

print("Rows written:", len(rows))

conn.close()

print("Done.")
