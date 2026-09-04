import streamlit as st

from services.get_network_statistics import (
    get_network_statistics
)

from services.get_classification_members_grouped import (
    get_classification_members_grouped
)

st.title("📡 Monitoring Network")

st.write(
    """
    Monitoring stations are classified
    using observed sampling behavior,
    parameters measured, and station
    fingerprints derived from DataStream.
    """
)

stats = get_network_statistics()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Stations",
        stats["total_stations"]
    )

    st.metric(
        "Profile Stations",
        stats["profile_stations"]
    )

with col2:

    st.metric(
        "Classifications",
        stats["total_classifications"]
    )

    st.metric(
        "Bacteria Stations",
        stats["bacteria_stations"]
    )

with col3:

    st.metric(
        "Max Parameters",
        stats["max_parameters"]
    )

    st.metric(
        "Deepest Sample",
        f"{abs(stats['deepest_sample'])} m"
    )

st.divider()


data = get_classification_members_grouped()

for classification, stations in data.items():

    with st.expander(
    f"{classification} ({len(stations)})",
    expanded=False
):

        for station in stations:
        
            st.write(
                f"**{station['monitoring_location_id']}** "
                f"(Parameters: {station['parameter_count']}, "
                f"Depth Levels: {station['depth_count']})"
            )

        st.divider()