import streamlit as st
import pandas as pd
import plotly.express as px
import networkx as nx
import plotly.graph_objects as go

st.set_page_config(page_title="Data Privacy Dashboard", layout="wide")

st.title("📊 Enterprise Data Privacy Monitoring Dashboard")

st.write("A prototype dashboard showing breach indicators, automated data flow mapping, and compliance monitoring.")

# ======================================
# SECTION 1 — BREACH INDICATOR MONITORING
# ======================================
st.subheader("🔐 Breach Indicator Monitoring")

alerts = pd.DataFrame({
    "Indicator": ["Unusual Login Location", "Missing 2FA", "Lateral Movement Detected", "Data Exfiltration Spike"],
    "Status": ["Flagged", "Critical", "Flagged", "Warning"],
    "Details": [
        "Login from unapproved region (Egypt)",
        "Server-14 missing two-factor authentication",
        "User accessed 90+ servers (anomalous)",
        "Large outbound data transfers observed"
    ]
})

st.dataframe(alerts, use_container_width=True)

# ======================================
# SECTION 2 — AUTOMATED DATA FLOW MAPPING
# ======================================
st.subheader("🌐 Automated Data Flow Mapping")
st.markdown("Simple and stable visual showing normal data flow and suspicious exfiltration.")

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 2))

# Nodes
nodes = ["User Login", "Internal App", "Data Server", "Finance DB", "External IP"]
x_positions = [0.1, 0.3, 0.5, 0.7, 0.9]

# Draw nodes (boxes)
for x, label in zip(x_positions, nodes):
    box_color = "red" if label == "External IP" else "lightgray"
    ax.text(x, 0.5, label, ha="center", va="center", fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", fc=box_color))

# Draw arrows between nodes
for i in range(len(x_positions)-1):
    ax.annotate(
        "",
        xy=(x_positions[i+1]-0.04, 0.5),
        xytext=(x_positions[i]+0.04, 0.5),
        arrowprops=dict(arrowstyle="->", lw=2)
    )

ax.set_axis_off()
st.pyplot(fig)


# ======================================
# SECTION 3 — COMPLIANCE MONITORING
# ======================================
st.subheader("📋 Compliance Monitoring Overview")

compliance = pd.DataFrame({
    "Check": ["Data Retention", "Access Controls", "Encryption", "Audit Logging", "Anomaly Detection"],
    "Status": ["Pass", "Fail", "Pass", "Fail", "Flagged"],
    "Notes": [
        "All data within 7-year retention",
        "Server-14 missing 2FA",
        "Encryption enabled on major DBs",
        "Logs missing on 3 servers",
        "User behavior anomaly detected"
    ]
})

st.table(compliance)

st.success("Prototype dashboard loaded successfully.")
