import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="JP Morgan Chase 2014 Data Breach",
    layout="wide"
)

st.title("🏦 JP Morgan Chase 2014 Data Breach — Dashboard")
st.write(
    "This dashboard summarizes the 2014 JP Morgan data breach, its impact, "
    "attack progression, and compliance failures using analytical monitoring views."
)

# ======================================================
# BREACH OVERVIEW
# ======================================================
st.subheader("🚨 Breach Overview")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Accounts Affected", "83 Million")
c2.metric("Households Impacted", "76 Million")
c3.metric("Undetected For", "60 Days")
c4.metric("Financial Fraud", "$0")

st.markdown("---")

# ======================================================
# ATTACK TIMELINE
# ======================================================
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

# ======================================================
# HOW THE ATTACK HAPPENED
# ======================================================
st.subheader("🧠 How the Attack Happened")

steps = [
    "Phishing email compromises employee credentials",
    "Credentials reused to access internal systems",
    "Server without multi-factor authentication exploited",
    "Privilege escalation to administrator level",
    "Lateral movement across 90+ internal servers",
    "Gradual data exfiltration over a 60-day period"
]

for s in steps:
    st.markdown(f"➡️ {s}")

st.markdown("---")

# ======================================================
# BREACH INDICATOR MONITORING
# ======================================================
st.subheader("🔐 Breach Indicator Monitoring")

indicators = pd.DataFrame({
    "Indicator": [
        "Unusual login location",
        "Missing multi-factor authentication",
        "Excessive lateral movement",
        "Sustained outbound data transfers"
    ],
    "Status": ["Flagged", "Critical", "Flagged", "Warning"],
    "Details": [
        "Login from unapproved foreign region",
        "Critical server missing MFA protection",
        "User accessed 90+ internal servers",
        "Abnormal outbound traffic spike detected"
    ]
})

st.dataframe(indicators, width="stretch")

st.markdown("---")

# ======================================================
# AUTOMATED DATA FLOW MAPPING (MUTED COLORS)
# ======================================================
st.subheader("🌐 Automated Data Flow Mapping")

labels = [
    "Employee Login",
    "Internal Application",
    "Core Database",
    "Data Warehouse",
    "External IP"
]

source = [0, 1, 2, 3]
target = [1, 2, 3, 4]
value  = [10, 10, 8, 6]

# Muted / low-brightness colors
colors = [
    "rgba(140,180,140,0.6)",   # normal internal flow
    "rgba(140,180,140,0.6)",
    "rgba(200,170,120,0.6)",   # elevated privilege
    "rgba(190,120,120,0.6)"    # exfiltration
]

fig = go.Figure(go.Sankey(
    node=dict(
        pad=18,
        thickness=18,
        line=dict(color="gray", width=0.5),
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
    height=320
)

st.plotly_chart(fig, width="stretch")

st.caption(
    "Flow visualization highlights normal internal data movement and a high-risk "
    "exfiltration path from internal systems to an external IP."
)

st.markdown("---")

# ======================================================
# COMPLIANCE MONITORING
# ======================================================
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
        "Critical servers lacked MFA",
        "Customer data encrypted",
        "Incomplete logging across systems",
        "Behavior anomalies detected late"
    ]
})

st.table(compliance)

st.success("Dashboard loaded successfully.")
