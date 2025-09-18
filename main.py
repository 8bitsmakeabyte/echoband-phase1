import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import random

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="EchoBand Dashboard",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------
st.markdown(
    """
    <div style="background-color:black; padding:12px; text-align:center;">
        <h2 style="color:white; margin:0;">EchoBand – Emergency Dashboard</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------------
# Layout: Two columns
# ----------------------------
left_col, right_col = st.columns([2,1])  # more space for map

# ----------------------------
# LEFT SIDE
# ----------------------------
with left_col:
    st.subheader("Device Status")

    # Flip Active/Inactive randomly for demo
    band_active = random.choice([True, False])

    status_color = "red" if band_active else "green"
    status_text = "ACTIVE – Emergency Mode" if band_active else "INACTIVE – Normal Mode"

    st.markdown(
        f"""
        <div style="background-color:{status_color}; 
                    padding:20px; 
                    border-radius:10px; 
                    text-align:center; 
                    font-size:18px; 
                    font-weight:bold; 
                    color:white;">
            {status_text}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Incident Log")

    # Expanded Incident Log
    data = {
        "Date & Time": [
            "2025-09-15 18:32", "2025-09-14 22:11", "2025-09-12 21:00",
            "2025-09-10 17:45", "2025-09-07 20:10", "2025-09-05 19:30"
        ],
        "Trigger Type": ["Voice + HR", "HR only", "Voice + HR", "Voice only", "Voice + HR", "HR only"],
        "Peak BPM": [138, 125, 142, 98, 135, 122],
        "Duration (s)": [45, 30, 60, 20, 50, 25],
        "GPS Location": [
            "19.1176, 72.9060", "19.1120, 72.9081", "19.1200, 72.9099",
            "19.1190, 72.9075", "19.1150, 72.9055", "19.1165, 72.9020"
        ],
        "Audio": ["Play/Download"] * 6,
        "Status": ["Acknowledged", "Escalated", "Acknowledged", "Auto-cleared", "Escalated", "Acknowledged"],
        "Device Battery": ["78%", "54%", "65%", "80%", "40%", "70%"],
        "Connectivity": ["Online", "Offline", "Online", "Online", "Online", "Online"],
        "Acknowledged By": ["Mom", "—", "Dad", "—", "Best Friend", "Mom"],
        "Remarks": [
            "False alarm ruled out", "Needs follow-up", "Situation resolved",
            "False trigger (voice only)", "Contacted local police", "Panic attack (medical)"
        ]
    }
    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True, height=250)

# ----------------------------
# RIGHT SIDE
# ----------------------------
with right_col:
    st.subheader("Last Known Location")

    # Hardcoded coordinates (Powai, Mumbai for example)
    latitude, longitude = 19.1176, 72.9060

    m = folium.Map(location=[latitude, longitude], zoom_start=15)
    folium.Marker(
        [latitude, longitude],
        popup="Last Location",
        tooltip="EchoBand User",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

    st_folium(m, width=750, height=500)  # wider map, more centered

# ----------------------------
# Emergency Contacts Section
# ----------------------------
st.subheader("Emergency Contacts")

contacts = {
    "Name": ["Mom", "Dad", "Best Friend", "Local Police"],
    "Phone": ["+91-9876543210", "+91-9123456780", "+91-9988776655", "100"],
    "Relation": ["Primary Contact", "Secondary Contact", "Friend", "Authority"],
    "Status": ["Active", "Active", "Active", "Available"]
}
df_contacts = pd.DataFrame(contacts)

st.table(df_contacts)
