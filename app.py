import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="First Lake Watch",
    page_icon="🌊",
    layout="wide"
)

# --------------------------------------------------
# Sample Data
# --------------------------------------------------

data = {
    "Date": [
        "2024-05-01", "2024-06-01", "2024-07-01", "2024-08-01",
        "2024-05-01", "2024-06-01", "2024-07-01", "2024-08-01",
        "2024-05-01", "2024-06-01", "2024-07-01", "2024-08-01",
        "2024-05-01", "2024-06-01", "2024-07-01", "2024-08-01"
    ],
    "Parameter": [
        "Temperature", "Temperature", "Temperature", "Temperature",
        "pH", "pH", "pH", "pH",
        "Dissolved Oxygen", "Dissolved Oxygen", "Dissolved Oxygen", "Dissolved Oxygen",
        "Conductivity", "Conductivity", "Conductivity", "Conductivity"
    ],
    "Value": [
        11.5, 16.2, 21.1, 23.8,
        8.4, 8.2, 7.9, 7.95,
        13.2, 10.8, 8.6, 8.0,
        0.53, 0.49, 0.41, 0.46
    ]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🌊 First Lake Watch")

st.subheader(
    "Monitoring the health of First Lake, Lower Sackville, Nova Scotia"
)

# --------------------------------------------------
# Current Conditions
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("pH", "7.95")

with col2:
    st.metric("Temperature", "23.8°C")

with col3:
    st.metric("Dissolved Oxygen", "8.0 mg/L")

with col4:
    st.metric("Conductivity", "0.46 mS/cm")

st.divider()

# --------------------------------------------------
# Trends
# --------------------------------------------------

st.header("Water Quality Trends")

parameter = st.selectbox(
    "Select Parameter",
    [
        "Temperature",
        "pH",
        "Dissolved Oxygen",
        "Conductivity"
    ]
)

filtered_df = df[df["Parameter"] == parameter]

fig = px.line(
    filtered_df,
    x="Date",
    y="Value",
    markers=True,
    title=f"{parameter} Trend"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# --------------------------------------------------
# Lake Health
# --------------------------------------------------

st.header("Lake Health")

st.success("🟢 GOOD")

st.write(
    "Community water quality indicator based on available monitoring data."
)

st.divider()

# --------------------------------------------------
# Status
# --------------------------------------------------

st.info(
    "Atlantic DataStream API integration pending approval."
)