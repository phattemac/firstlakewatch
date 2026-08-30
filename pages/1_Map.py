import streamlit as st
import folium
from streamlit_folium import st_folium
from datetime import datetime
import pandas as pd
import plotly.express as px

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
    return "red"


def status_icon(color):
    icons = {
        "green": "🟢",
        "yellow": "🟡",
        "orange": "🟠",
        "red": "🔴"
    }
    return icons.get(color, "⚪")


# --------------------------------------------------
# Sample Stations
# --------------------------------------------------

stations = [
    {
        "name": "Deep Basin",
        "lat": 44.7725,
        "lon": -63.6685,
        "sample_date": "2026-08-24",
        "ecoli": 4,
        "ph": 7.9,
        "do": 8.0,
        "temp": 23.8,
        "cond": 0.46
    },
    {
        "name": "Beach Area",
        "lat": 44.7739,
        "lon": -63.6710,
        "sample_date": "2026-08-20",
        "ecoli": 18,
        "ph": 8.1,
        "do": 7.5,
        "temp": 24.1,
        "cond": 0.51
    },
    {
        "name": "Sucker Brook",
        "lat": 44.7692,
        "lon": -63.6595,
        "sample_date": "2026-08-15",
        "ecoli": 125,
        "ph": 7.2,
        "do": 5.9,
        "temp": 21.0,
        "cond": 0.63
    }
]

# --------------------------------------------------
# Historical Data
# --------------------------------------------------

historical_data = {
    "Deep Basin": {
        "Date": ["2026-05-01", "2026-06-01", "2026-07-01", "2026-08-24"],
        "E.coli": [2, 3, 5, 4],
        "pH": [8.1, 8.0, 7.8, 7.9],
        "DO": [10.5, 9.2, 8.7, 8.0],
        "Temperature": [11.5, 16.2, 21.1, 23.8]
    },
    "Beach Area": {
        "Date": ["2026-05-01", "2026-06-01", "2026-07-01", "2026-08-20"],
        "E.coli": [10, 15, 20, 18],
        "pH": [8.2, 8.1, 8.0, 8.1],
        "DO": [9.8, 8.8, 7.9, 7.5],
        "Temperature": [12.0, 17.5, 22.3, 24.1]
    },
    "Sucker Brook": {
        "Date": ["2026-05-01", "2026-06-01", "2026-07-01", "2026-08-15"],
        "E.coli": [40, 60, 90, 125],
        "pH": [7.4, 7.3, 7.3, 7.2],
        "DO": [7.1, 6.5, 6.1, 5.9],
        "Temperature": [10.5, 15.8, 19.5, 21.0]
    }
}

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "selected_station" not in st.session_state:
    st.session_state.selected_station = "Deep Basin"

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

        color = ecoli_color(station["ecoli"])

        radius = 18 if (
            station["name"]
            == st.session_state.selected_station
        ) else 10

        folium.CircleMarker(
            location=[station["lat"], station["lon"]],
            radius=radius,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8,
            tooltip=station["name"],
            popup=station["name"]
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
    station
    for station in stations
    if station["name"] == st.session_state.selected_station
)

sample_date = datetime.strptime(
    selected_station["sample_date"],
    "%Y-%m-%d"
)

days_old = (
    datetime.now() - sample_date
).days

# --------------------------------------------------
# DETAILS PANEL
# --------------------------------------------------

with col2:

    st.header(selected_station["name"])

    st.metric(
        "Last Sample",
        selected_station["sample_date"]
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

    ecoli_status = ecoli_color(
        selected_station["ecoli"]
    )

    st.write(
        f"{status_icon(ecoli_status)} E. coli: {selected_station['ecoli']} CFU/100mL"
    )

    ph_status = (
        "green"
        if 6.5 <= selected_station["ph"] <= 8.5
        else "red"
    )

    st.write(
        f"{status_icon(ph_status)} pH: {selected_station['ph']}"
    )

    do_status = (
        "green"
        if selected_station["do"] >= 8
        else "yellow"
        if selected_station["do"] >= 6
        else "red"
    )

    st.write(
        f"{status_icon(do_status)} Dissolved Oxygen: {selected_station['do']} mg/L"
    )

    temp_status = (
        "green"
        if selected_station["temp"] < 25
        else "orange"
    )

    st.write(
        f"{status_icon(temp_status)} Temperature: {selected_station['temp']} °C"
    )

    cond_status = (
        "green"
        if selected_station["cond"] < 0.5
        else "yellow"
        if selected_station["cond"] < 0.75
        else "red"
    )

    st.write(
        f"{status_icon(cond_status)} Conductivity: {selected_station['cond']} mS/cm"
    )

    st.divider()

    st.subheader("Historical Trend")

    chart_parameter = st.selectbox(
        "Parameter",
        [
            "E.coli",
            "pH",
            "DO",
            "Temperature"
        ]
    )

    station_history = historical_data[
        selected_station["name"]
    ]

    chart_df = pd.DataFrame({
        "Date": station_history["Date"],
        "Value": station_history[chart_parameter]
    })

    fig = px.line(
        chart_df,
        x="Date",
        y="Value",
        markers=True,
        title=f"{selected_station['name']} - {chart_parameter}"
    )

    st.plotly_chart(fig)

    st.divider()

    st.subheader("Monitoring Location")

    st.write(f"Latitude: {selected_station['lat']}")
    st.write(f"Longitude: {selected_station['lon']}")

    st.divider()

    if selected_station["ecoli"] > 100:
        st.error("🔴 Overall Status: Poor")
    elif selected_station["ecoli"] > 50:
        st.warning("🟠 Overall Status: Fair")
    else:
        st.success("🟢 Overall Status: Good")