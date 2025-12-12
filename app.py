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
st.markdown("Clean visual showing normal data flow and suspicious exfiltration path.")

import plotly.graph_objects as go

# Create the flowchart layout
fig = go.Figure()

nodes = ["User Login", "Internal App", "Data Server", "Finance DB", "External IP"]
x_positions = [0, 0.25, 0.50, 0.75, 1.0]

# Add normal nodes (grey)
for i, label in enumerate(nodes[:-1]):
    fig.add_trace(go.Scatter(
        x=[x_positions[i]],
        y=[0.5],
        mode="text",
        text=[label],
        textposition="middle center",
        textfont=dict(size=16, color="black")
    ))
    fig.add_shape(
        type="rect",
        x0=x_positions[i]-0.07, y0=0.4,
        x1=x_positions[i]+0.07, y1=0.6,
        line=dict(color="black"),
        fillcolor="#E0E0E0"
    )

# Add suspicious node (External IP, red)
fig.add_trace(go.Scatter(
    x=[x_positions[-1]],
    y=[0.5],
    mode="text",
    text=[nodes[-1]],
    textposition="middle center",
    textfont=dict(size=16, color="white")
))
fig.add_shape(
    type="rect",
    x0=x_positions[-1]-0.07, y0=0.4,
    x1=x_positions[-1]+0.07, y1=0.6,
    line=dict(color="black"),
    fillcolor="red"
)

# Add arrows between nodes
for i in range(len(nodes)-1):
    fig.add_annotation(
        x=x_positions[i] + 0.125,
        y=0.5,
        ax=x_positions[i] + 0.02,
        ay=0.5,
        xref="paper", yref="paper",
        axref="paper", ayref="paper",
        showarrow=True,
        arrowhead=3,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="black"
    )

fig.update_layout(
    height=300,
    xaxis=dict(showgrid=False, zeroline=False, visible=False),
    yaxis=dict(showgrid=False, zeroline=False, visible=False),
    plot_bgcolor='white',
    paper_bgcolor='white',
    margin=dict(l=20, r=20, t=40, b=20)
)

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
