import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Current Conditions",
    page_icon="🌊",
    layout="wide"
)


# --------------------------------------------------
# HELPERS
# --------------------------------------------------

def get_featured_conditions():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        group_name,
        characteristic_name,
        sample_date,
        value,
        unit
    FROM featured_conditions
    ORDER BY
        group_name,
        characteristic_name
    """)

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows


def get_data_status():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        group_name,
        MAX(sample_date) AS latest_date
    FROM featured_conditions
    GROUP BY group_name
    """)

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows


def get_group_conditions(group_name):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        characteristic_name,
        sample_date,
        value,
        unit
    FROM featured_conditions
    WHERE group_name = ?
    ORDER BY characteristic_name
    """,
    (group_name,)
    )

    rows = [
        dict(row)
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows


# --------------------------------------------------
# PAGE
# --------------------------------------------------

st.title("🌊 Current Conditions")

st.markdown(
    """
    Current conditions are derived from the
    featured monitoring stations discovered
    through Atlantic DataStream.
    """
)

# --------------------------------------------------
# DATA FRESHNESS
# --------------------------------------------------

st.header("📅 Data Freshness")

status_rows = get_data_status()

cols = st.columns(
    len(status_rows)
)

for i, row in enumerate(status_rows):

    with colsst.metric(
            row["group_name"].replace(
                "_",
                " "
            ).title(),
            row["latest_date"]
        )

# --------------------------------------------------
# DEEP WATER
# --------------------------------------------------

st.header("🔵 Deep Water Conditions")

deep_rows = get_group_conditions(
    "deep_water"
)

if deep_rows:

    for row in deep_rows:

        name = row[
            "characteristic_name"
        ]

        value = row["value"]

        unit = row["unit"]

        if name == "pH":

            st.metric(
                "pH",
                value
            )

        elif (
            name
            ==
            "Dissolved oxygen (DO)"
        ):

            st.metric(
                "Dissolved Oxygen",
                f"{value} {unit}"
            )

        elif (
            name
            ==
            "Temperature, water"
        ):

            st.metric(
                "Water Temperature",
                f"{value} °C"
            )

        elif (
            name
            ==
            "Chlorophyll a, corrected for pheophytin"
        ):

            st.metric(
                "Chlorophyll a",
                f"{value} {unit}"
            )

        elif (
            name
            ==
            "Total Phosphorus, mixed forms"
        ):

            st.metric(
                "Total Phosphorus",
                f"{value} {unit}"
            )

# --------------------------------------------------
# SURFACE
# --------------------------------------------------

st.header("🟢 Surface Conditions")

surface_rows = get_group_conditions(
    "surface"
)

if surface_rows:

    col1, col2 = st.columns(2)

    for i, row in enumerate(surface_rows):

        target_col = (
            col1
            if i % 2 == 0
            else col2
        )

        with target_col:

            st.metric(
                row[
                    "characteristic_name"
                ],
                row["value"]
            )

# --------------------------------------------------
# INFLOW / OUTFLOW
# --------------------------------------------------

st.header("➡️ Watershed Conditions")

left, right = st.columns(2)

with left:

    st.subheader("Inflow")

    inflow_rows = get_group_conditions(
        "inflow"
    )

    for row in inflow_rows:

        st.write(
            f"**{row['characteristic_name']}**"
            f": {row['value']} "
            f"{row['unit']}"
        )

with right:

    st.subheader("Outflow")

    outflow_rows = get_group_conditions(
        "outflow"
    )

    for row in outflow_rows:

        st.write(
            f"**{row['characteristic_name']}**"
            f": {row['value']} "
            f"{row['unit']}"
        )

# --------------------------------------------------
# BACTERIA PROGRAM
# --------------------------------------------------

st.header("🦠 Bacteria Monitoring")

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    monitoring_location_id,
    classification
FROM station_classifications
WHERE classification = 'BACTERIA'
ORDER BY monitoring_location_id
""")

rows = cursor.fetchall()

conn.close()

st.write(
    f"Monitoring Stations: {len(rows)}"
)

for station_id, classification in rows:

    st.write(
        f"• {station_id}"
    )

# --------------------------------------------------
# NETWORK OVERVIEW
# --------------------------------------------------

st.header("📡 Monitoring Network")

conn = sqlite3.connect(
    "database/firstlake.db"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    classification,
    COUNT(*)
FROM station_classifications
GROUP BY classification
ORDER BY classification
""")

rows = cursor.fetchall()

conn.close()

for classification, count in rows:

    st.write(
        f"**{classification}**: {count}"
    )