import pandas as pd

# Load the First Lake CSV
df = pd.read_csv(
    "doi.org_10.25976_may9-2452.csv",
    low_memory=False
)

# Keep only the location fields
locations = df[
    [
        "MonitoringLocationID",
        "MonitoringLocationName",
        "MonitoringLocationLatitude",
        "MonitoringLocationLongitude"
    ]
]

# Remove duplicates
locations = locations.drop_duplicates()

# Sort for easier review
locations = locations.sort_values(
    by=["MonitoringLocationID"]
)

print()
print("Unique First Lake Monitoring Locations")
print("=" * 50)
print()

for _, row in locations.iterrows():

    print(
        f"{row['MonitoringLocationID']} | "
        f"{row['MonitoringLocationName']} | "
        f"{row['MonitoringLocationLatitude']} | "
        f"{row['MonitoringLocationLongitude']}"
    )

print()
print(f"Total Locations: {len(locations)}")

# Save to CSV
locations.to_csv(
    "database/first_lake_locations.csv",
    index=False
)

print()
print(
    "Saved to database/first_lake_locations.csv"
)