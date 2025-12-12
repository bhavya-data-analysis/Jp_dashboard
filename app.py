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
# SECTION 2 — AUTOMATED DATA FLOW MAP
# ======================================
st.subheader("🌐 Automated Data Flow Mapping")

st.markdown("This visual shows how data normally flows inside the system, and where a suspicious exfiltration path appears.")

# SIMPLE AND SAFE SANKEY NODES
labels = ["User Login", "Internal App", "Data Server", "Finance DB", "External IP"]

# Normal flows (grey)
source = [0, 1, 2]
target = [1, 2, 3]
value  = [1, 1, 1]
color  = ["#A0A0A0", "#A0A0A0", "#A0A0A0"]  # grey links

# Add suspicious RED link (Finance DB → External IP)
source.append(3)
target.append(4)
value.append(1)
color.append("red")

fig = go.Figure(data=[go.Sankey(
    node=dict(
        label=labels,
        pad=20,
        thickness=20,
        color="lightblue"
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=color
    )
)])

fig.update_layout(title_text="Data Flow Visualization", height=400)

st.plotly_chart(fig, use_container_width=True)


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
