import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sqlite3

from services.get_profile_dates import (
    get_profile_dates
)

from services.get_profile_data import (
    get_profile_data
)

st.title("🌊 Lake Profiles")

# ----------------------------------
# STATIONS
# ----------------------------------

conn = sqlite3.connect(
    "database/firstlake.db"
)

stations = pd.read_sql_query(
    """
    SELECT monitoring_location_id
    FROM station_classifications
    WHERE classification IN
    (
        'PROFILE',
        'INTENSIVE_PROFILE'
    )
    ORDER BY monitoring_location_id
    """,
    conn
)

conn.close()

station = st.selectbox(
    "Station",
    stations[
        "monitoring_location_id"
    ].tolist()
)

# ----------------------------------
# DATE SLIDER
# ----------------------------------

dates = get_profile_dates(
    station
)

selected_date = st.select_slider(
    "Profile Date",
    options=dates,
    value=dates[-1]
)

# ----------------------------------
# PARAMETERS
# ----------------------------------

st.subheader(
    "Parameters"
)

col1, col2 = st.columns(2)

with col1:

    show_do = st.checkbox(
        "Dissolved Oxygen",
        value=True
    )

    show_temp = st.checkbox(
        "Temperature",
        value=True
    )

with col2:

    show_ph = st.checkbox(
        "pH"
    )

    show_cond = st.checkbox(
        "Conductivity"
    )

# ----------------------------------
# PROFILE DATA
# ----------------------------------

df = get_profile_data(
    station,
    selected_date
)

if df.empty:

    st.warning(
        "No profile data found."
    )

    st.stop()

df["depth"] = pd.to_numeric(
    df["depth"],
    errors="coerce"
)

df["value"] = pd.to_numeric(
    df["value"],
    errors="coerce"
)

df["depth_m"] = (
    df["depth"].abs()
)

# ----------------------------------
# CHART
# ----------------------------------

fig = go.Figure()

if show_do:

    do_df = df[
        df["characteristic_name"]
        ==
        "Dissolved oxygen (DO)"
    ]

    fig.add_trace(
        go.Scatter(
            x=do_df["value"],
            y=do_df["depth_m"],
            mode="lines+markers",
            name="DO"
        )
    )

if show_temp:

    temp_df = df[
        df["characteristic_name"]
        ==
        "Temperature, water"
    ]

    fig.add_trace(
        go.Scatter(
            x=temp_df["value"],
            y=temp_df["depth_m"],
            mode="lines+markers",
            name="Temperature"
        )
    )

if show_ph:

    ph_df = df[
        df["characteristic_name"]
        ==
        "pH"
    ]

    fig.add_trace(
        go.Scatter(
            x=ph_df["value"],
            y=ph_df["depth_m"],
            mode="lines+markers",
            name="pH"
        )
    )

if show_cond:

    cond_df = df[
        df["characteristic_name"]
        ==
        "Specific conductance"
    ]

    fig.add_trace(
        go.Scatter(
            x=cond_df["value"],
            y=cond_df["depth_m"],
            mode="lines+markers",
            name="Conductivity"
        )
    )

fig.update_layout(
    height=700,
    title=f"{station} | {selected_date}",
    xaxis_title="Value",
    yaxis_title="Depth (m)"
)

fig.update_yaxes(
    autorange="reversed"
)

st.plotly_chart(
    fig,
    use_container_width=True
)