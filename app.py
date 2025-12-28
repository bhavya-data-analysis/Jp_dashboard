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

st.subheader("🌐 Automated Data Flow Mapping")

# KPI-style summary row
c1, c2, c3 = st.columns(3)
c1.metric("Normal Flows", "2")
c2.metric("High-Risk Flows", "1")
c3.metric("Critical Exfiltration Points", "1")

st.markdown("#### Identified Data Movement Paths")

flow = pd.DataFrame({
    "Flow Path": [
        "Employee Login → Internal Application",
        "Internal Application → Core Database",
        "Core Database → Data Warehouse",
        "Data Warehouse → External IP"
    ],
    "Risk Level": [
        "Normal",
        "Normal",
        "High Privilege Access",
        "Suspicious Exfiltration"
    ]
})

st.table(flow)

st.caption(
    "Analysis highlights a high-risk data movement from internal storage to an external IP, "
    "indicating a potential exfiltration point."
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
