import streamlit as st
import sqlite3


# --------------------------------------------------
# DATABASE HELPERS
# --------------------------------------------------

def get_station_list():

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            monitoring_location_id
        FROM station_fingerprints
        ORDER BY monitoring_location_id
        """
    )

    rows = [
        row[0]
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows


def get_station_details(
    station_id
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            sf.monitoring_location_id,
            sf.datastream_id,
            sf.location_name,
            sf.parameter_count,
            sf.depth_count,
            sf.deepest_sample,
            sf.shallowest_sample,
            sf.has_ecoli,
            sf.has_secchi,
            sf.has_chlorophyll,
            sf.has_phosphorus,
            sc.classification
        FROM station_fingerprints sf
        LEFT JOIN station_classifications sc
            ON sf.monitoring_location_id =
               sc.monitoring_location_id
        WHERE sf.monitoring_location_id = ?
        """,
        (station_id,)
    )

    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)

    return None


def get_station_characteristics(
    station_id
):

    conn = sqlite3.connect(
        "database/firstlake.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            characteristic_name
        FROM station_characteristics
        WHERE monitoring_location_id = ?
        ORDER BY characteristic_name
        """,
        (station_id,)
    )

    rows = [
        row[0]
        for row in cursor.fetchall()
    ]

    conn.close()

    return rows


# --------------------------------------------------
# PAGE
# --------------------------------------------------

st.title("🔬 Station Details")

stations = get_station_list()

selected_station = st.selectbox(
    "Select Station",
    stations
)

details = get_station_details(
    selected_station
)

if not details:

    st.error(
        "Station not found."
    )

    st.stop()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.header(
    details["monitoring_location_id"]
)

st.write(
    f"**Name:** {details['location_name']}"
)

st.write(
    f"**Classification:** "
    f"{details['classification']}"
)

# --------------------------------------------------
# KEY METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Parameters",
        details["parameter_count"]
    )

    st.metric(
        "Depth Levels",
        details["depth_count"]
    )

with col2:

    st.metric(
        "DataStream ID",
        details["datastream_id"]
    )

    st.metric(
        "Deepest Sample",
        abs(
            details["deepest_sample"]
        )
        if details["deepest_sample"]
        is not None
        else "N/A"
    )

with col3:

    st.metric(
        "E. coli",
        "Yes"
        if details["has_ecoli"]
        else "No"
    )

    st.metric(
        "Secchi",
        "Yes"
        if details["has_secchi"]
        else "No"
    )

# --------------------------------------------------
# CAPABILITIES
# --------------------------------------------------

st.header("📋 Monitoring Capabilities")

capabilities = []

if details["has_ecoli"]:
    capabilities.append(
        "Escherichia coli"
    )

if details["has_secchi"]:
    capabilities.append(
        "Secchi Depth"
    )

if details["has_chlorophyll"]:
    capabilities.append(
        "Chlorophyll"
    )

if details["has_phosphorus"]:
    capabilities.append(
        "Phosphorus"
    )

if capabilities:

    for item in capabilities:

        st.write(
            f"✅ {item}"
        )

else:

    st.write(
        "No special capabilities identified."
    )

# --------------------------------------------------
# DEPTH PROFILE
# --------------------------------------------------

st.header("📏 Sampling Profile")

st.write(
    f"Depth Levels: "
    f"{details['depth_count']}"
)

if details["deepest_sample"] is not None:

    st.write(
        f"Deepest Sample: "
        f"{abs(details['deepest_sample'])} m"
    )

if details["shallowest_sample"] is not None:

    st.write(
        f"Shallowest Sample: "
        f"{abs(details['shallowest_sample'])} m"
    )

# --------------------------------------------------
# PARAMETERS
# --------------------------------------------------

st.header("🧪 Measured Parameters")

characteristics = get_station_characteristics(
    selected_station
)

st.write(
    f"Total Parameters: "
    f"{len(characteristics)}"
)

for characteristic in characteristics:

    st.write(
        f"• {characteristic}"
    )