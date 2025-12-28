import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="JP Morgan Chase 2014 Data Breach", layout="wide")

st.title("🏦 JP Morgan Chase 2014 Data Breach — Dashboard")
st.write(
    "This dashboard summarizes the 2014 JP Morgan data breach, its impact, failures, "
    "and how analytics could have detected it earlier."
)

# ======================================
# BREACH OVERVIEW
# ======================================
st.subheader("🚨 Breach Overview")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Accounts Affected", "83 Million")
c2.metric("Households Impacted", "76 Million")
c3.metric("Undetected For", "60 Days")
c4.metric("Financial Fraud", "$0")

st.markdown("---")

# ======================================
# ATTACK TIMELINE
# ======================================
st.subheader("🕒 Attack Timeline")

timeline = pd.DataFrame({
    "Event": [
        "Breach begins",
        "Attackers active",
        "External detection",
        "Breach contained",
        "Public disclosure"
    ],
    "Date": [
        "June 2014",
        "Jun–Aug 2014",
        "Late July 2014",
        "Mid-Aug 2014",
        "Oct 2, 2014"
    ]
})

st.table(timeline)

st.markdown("---")

# ======================================
# HOW THE ATTACK HAPPENED
# ======================================
st.subheader("🧠 How the Attack Happened")

attack_steps = [
    "Phishing email compromises employee credentials",
    "Credentials stolen and reused",
    "Server without two-factor authentication exploited",
    "Privilege escalation to administrator level",
    "Lateral movement across 90+ servers",
    "Gradual data exfiltration over 60 days"
]

for step in attack_steps:
    st.markdown(f"➡️ {step}")

st.markdown("---")

# ======================================
# BREACH INDICATOR MONITORING
# ======================================
st.subheader("🔐 Breach Indicator Monitoring")

indicators = pd.DataFrame({
    "Indicator": [
        "Unusual login location",
        "Missing two-factor authentication",
        "Excessive lateral movement",
        "Sustained outbound data transfers"
    ],
    "Status": ["Flagged", "Critical", "Flagged", "Warning"],
    "Details": [
        "Login from unapproved foreign region",
        "Critical server missing 2FA protection",
        "User accessed 90+ internal servers",
        "Abnormal outbound traffic spike detected"
    ]
})

st.dataframe(indicators, use_container_width=True)

st.markdown("---")

# ======================================
# AUTOMATED DATA FLOW MAPPING
# ======================================

import plotly.graph_objects as go

st.subheader("🌐 Automated Data Flow Mapping")

labels = [
    "Employee Login",
    "Internal Application",
    "Core Database",
    "Data Warehouse",
    "External IP"
]

# index mapping
source = [0, 1, 2, 3]
target = [1, 2, 3, 4]
value  = [10, 10, 8, 6]

colors = [
    "rgba(100,200,100,0.8)",  # normal
    "rgba(100,200,100,0.8)",  # normal
    "rgba(255,165,0,0.8)",    # high privilege
    "rgba(255,0,0,0.8)"       # exfiltration
]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=20,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=colors
    )
))

fig.update_layout(
    title_text="Data Movement Across Systems",
    font_size=12,
    height=300
)

st.plotly_chart(fig, use_container_width=True)

st.caption(
    "Flow visualization highlights normal internal data movement and a high-risk "
    "exfiltration path to an external IP."
)


# ======================================
# COMPLIANCE MONITORING
# ======================================
st.subheader("📋 Compliance Monitoring Overview")

compliance = pd.DataFrame({
    "Control": [
        "Access Controls",
        "Multi-Factor Authentication",
        "Encryption at Rest",
        "Audit Logging",
        "Anomaly Detection"
    ],
    "Status": [
        "Partial",
        "Fail",
        "Pass",
        "Fail",
        "Flagged"
    ],
    "Notes": [
        "Over-privileged user accounts detected",
        "Critical servers lacked 2FA",
        "Customer data encrypted",
        "Incomplete logging across systems",
        "Behavior anomalies detected late"
    ]
})

st.table(compliance)

st.success("Dashboard loaded successfully.")
