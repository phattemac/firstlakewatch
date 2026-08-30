import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
import pandas as pd
import plotly.express as px

from services.samples import get_sample_history
from services.latest_samples import get_latest_ecoli
from services.stations import get_stations

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------

def ecoli_color(value):
    if value <= 10:
        return "green"
    elif value <= 50:
        return "yellow"
    elif value <= 100:
        return "orange"
    else:
        return "red"


def status_icon(color):
    return {
        "green": "🟢",
        "yellow": "🟡",
        "orange": "🟠",
        "red": "🔴"
    }.get(color, "⚪")


# --------------------------------------------------
# Load Stations
# --------------------------------------------------

stations = get_stations()

if "selected_station" not in st.session_state:
    st.session_state.selected_station = stations[0]["name"]

# --------------------------------------------------
# Page Header
# --------------------------------------------------

st.title("🗺️ Monitoring Locations")

col1, col2 = st.columns([3, 1])

# --------------------------------------------------
# MAP
# --------------------------------------------------

with col1:

    first_lake = [44.7738, -63.6675]

    m = folium.Map(
        location=first_lake,
        zoom_start=15,
        tiles=None
    )

    folium.TileLayer(
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="Esri Satellite"
    ).add_to(m)

    bounds = [
        [44.7665, -63.6780],
        [44.7805, -63.6540]
    ]

    m.fit_bounds(bounds)

    for station in stations:

        latest = get_latest_ecoli(station["id"])

        ecoli_value = latest["value"] if latest else 0

        color = ecoli_color(ecoli_value)

        radius = (
            18
            if station["name"] == st.session_state.selected_station
            else 10
        )

        folium.CircleMarker(
            location=[
                station["latitude"],
                station["longitude"]
            ],
            radius=radius,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            tooltip=station["name"],
            popup=f"{station['name']}<br>E.coli: {ecoli_value}"
        ).add_to(m)

    map_data = st_folium(
        m,
        width="stretch",
        height=700
    )

    if (
        map_data
        and map_data.get("last_object_clicked_tooltip")
    ):

        clicked_station = map_data[
            "last_object_clicked_tooltip"
        ]

        if clicked_station != st.session_state.selected_station:
            st.session_state.selected_station = clicked_station
            st.rerun()

# --------------------------------------------------
# Selected Station
# --------------------------------------------------

selected_station = next(
    s
    for s in stations
    if s["name"] == st.session_state.selected_station
)

latest = get_latest_ecoli(selected_station["id"])

sample_date = latest["sample_date"]
ecoli_value = latest["value"]

days_old = (
    datetime.now()
    - datetime.strptime(sample_date, "%Y-%m-%d")
).days

# --------------------------------------------------
# Details Panel
# --------------------------------------------------

with col2:

    st.header(selected_station["name"])

    st.metric(
        "Last Sample",
        sample_date
    )

    st.metric(
        "Days Since Sample",
        days_old
    )

    if days_old <= 7:
        st.success("🟢 Fresh Data")
    elif days_old <= 30:
        st.warning("🟡 Aging Data")
    else:
        st.error("🔴 Stale Data")

    st.divider()

    ecoli_status = ecoli_color(ecoli_value)

    st.write(
        f"{status_icon(ecoli_status)} E.coli: {ecoli_value} CFU/100mL"
    )

    st.write("⚪ pH: No data")
    st.write("⚪ Dissolved Oxygen: No data")
    st.write("⚪ Temperature: No data")
    st.write("⚪ Conductivity: No data")

    st.divider()

    st.subheader("Historical Trend")

    rows = get_sample_history(
        selected_station["id"],
        "E.coli"
    )

    chart_df = pd.DataFrame(rows)

    chart_df.rename(
        columns={
            "sample_date": "Date",
            "value": "Value"
        },
        inplace=True
    )

    fig = px.line(
        chart_df,
        x="Date",
        y="Value",
        markers=True,
        title=f"{selected_station['name']} - E.coli"
    )

    st.plotly_chart(fig)

    st.divider()

    st.subheader("Monitoring Location")

    st.write(
        f"Latitude: {selected_station['latitude']}"
    )

    st.write(
        f"Longitude: {selected_station['longitude']}"
    )

    st.divider()

    if ecoli_value > 100:
        st.error("🔴 Overall Status: Poor")
    elif ecoli_value > 50:
        st.warning("🟠 Overall Status: Fair")
    else:
        st.success("🟢 Overall Status: Good")