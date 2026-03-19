import streamlit as st
import pandas as pd
import os

LOG_FILE = "logs.txt"

st.title("Smart File Integrity Monitoring Dashboard")

st.write("Real-time security activity monitoring")

if os.path.exists(LOG_FILE):

    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    data = {"Events": logs}

    df = pd.DataFrame(data)

    st.subheader("Security Logs")

    st.dataframe(df)

    st.subheader("Total Events Detected")

    st.metric("Events", len(logs))

else:

    st.warning("No logs available yet")

st.subheader("System Status")

st.success("Monitoring system is active")

