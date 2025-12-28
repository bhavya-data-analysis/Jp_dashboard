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

fig, ax = plt.subplots(figsize=(10, 2))

nodes = ["Employee Login", "Internal App", "Core Database", "Data Warehouse", "External IP"]
x = [0.05, 0.25, 0.45, 0.65, 0.85]

for xpos, label in zip(x, nodes):
    color = "red" if label == "External IP" else "lightgray"
    ax.text(
        xpos, 0.5, label,
        ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.3", fc=color)
    )

for i in range(len(x) - 1):
    ax.annotate(
        "",
        xy=(x[i+1] - 0.04, 0.5),
        xytext=(x[i] + 0.04, 0.5),
        arrowprops=dict(arrowstyle="->", lw=2)
    )

ax.axis("off")
st.pyplot(fig)

st.markdown("---")

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
