import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
import pandas as pd
import plotly.express as px

from services.samples import get_sample_history
from services.latest_samples import get_latest_parameter
from services.stations import get_stations


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


stations = get_stations()

if not stations:
    st.error("No stations found in database.")
    st.stop()

if "selected_station" not in st.session_state:
    st.session_state.selected_station = stations[0]["name"]

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
        [44.7625, -63.6760],
        [44.7780, -63.6480]
    ]

    m.fit_bounds(bounds)

    # First Lake Monitoring Zone
    folium.Polygon(
        locations=[
            [44.7780, -63.6760], # northwest
            [44.7780, -63.6620], # top shoulder
            [44.7700, -63.6480], # northeast cut
            [44.7625, -63.6480], # southeas
            [44.7630, -63.6615], # move east again
            [44.7700, -63.6760] # move north on west side
            ],
        color="blue",
        weight=3,
        fill=True,
        fill_opacity=0.15,
        popup="First Lake Monitoring Zone"
    ).add_to(m)

    for station in stations:

        latest = get_latest_parameter(
            station["id"],
            "E.coli"
        )

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
# SELECTED STATION
# --------------------------------------------------

selected_station = next(
    s
    for s in stations
    if s["name"] == st.session_state.selected_station
)

latest_ecoli = get_latest_parameter(
    selected_station["id"],
    "E.coli"
)

latest_ph = get_latest_parameter(
    selected_station["id"],
    "pH"
)

sample_date = latest_ecoli["sample_date"]
ecoli_value = latest_ecoli["value"]

days_old = (
    datetime.now()
    - datetime.strptime(sample_date, "%Y-%m-%d")
).days

# --------------------------------------------------
# DETAILS PANEL
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

    ecoli_status = ecoli_color(
        ecoli_value
    )

    st.write(
        f"{status_icon(ecoli_status)} E.coli: {ecoli_value}"
    )

    if latest_ph:

        ph_value = latest_ph["value"]

        if 6.5 <= ph_value <= 8.5:
            ph_icon = "🟢"
        else:
            ph_icon = "🔴"

        st.write(
            f"{ph_icon} pH: {ph_value}"
        )

    else:

        st.write(
            "⚪ pH: No data"
        )

    st.write("⚪ Dissolved Oxygen: No data")
    st.write("⚪ Temperature: No data")
    st.write("⚪ Conductivity: No data")

    st.divider()

    st.subheader("Historical E.coli Trend")

    rows = get_sample_history(
        selected_station["id"],
        "E.coli"
    )

    chart_df = pd.DataFrame(rows)

    if not chart_df.empty:

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

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    st.subheader("Location")

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