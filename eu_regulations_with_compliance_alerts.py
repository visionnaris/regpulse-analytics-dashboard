import sqlite3
from datetime import datetime

# Step 1: Connect to the database
connection = sqlite3.connect("EU_Regulations.db")
cursor = connection.cursor()

# Step 2: Create the EU_Regulations table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS EU_Regulations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    regulation_article TEXT NOT NULL,
    framework TEXT NOT NULL,
    effective_date TEXT,
    department_impacted TEXT,
    key_focus TEXT,
    penalty_range TEXT
);
""")

# Step 3: Insert data (skip if already populated)
regulations_data = [
    ("Annex III (5)(b) – Creditworthiness Assessment", "EU AI Act", "2026-08-02", "Loans", "High-risk AI credit scoring; human oversight required", "€35M or 7% turnover"),
    ("Article 27 – Fundamental Rights Impact Assessment", "EU AI Act", "2026-08-02", "Loans/Deposits", "FRIA for AI systems affecting access to finance", "€20M or 4% turnover"),
    ("Article 50 – Transparency Obligations", "EU AI Act", "2026-12-02", "KYC", "Disclosure of automated decision-making to customers", "€10M or 2% turnover"),
    ("Articles 5–14 – ICT Risk Management", "DORA", "2025-01-17", "All Departments", "ICT resilience, incident reporting, third-party risk", "2% turnover"),
    ("Article 22 – Automated Decision-Making", "GDPR", "Ongoing", "Loans/KYC", "Human review for automated credit/KYC decisions", "€20M or 4% turnover"),
    ("Article 35 – Data Protection Impact Assessment", "GDPR", "Ongoing", "KYC/Deposits", "DPIA for high-risk personal data processing", "€10M or 2% turnover"),
    ("Annex III (1) – Biometric Identification Systems", "EU AI Act", "2026-08-02", "KYC", "Restricts facial recognition unless legally justified", "€35M or 7% turnover"),
    ("Article 9 – Risk Management System", "EU AI Act", "2026-08-02", "Loans/Deposits", "Continuous risk monitoring for AI models", "€20M or 4% turnover"),
    ("Article 14 – Human Oversight and Explainability", "EU AI Act", "2026-08-02", "Loans/Deposits", "Human intervention and explainable AI outputs", "€10M or 2% turnover"),
    ("Article 11 – Data Governance and Quality Management", "EU AI Act + GDPR", "2026-08-02", "All Departments", "High-quality, unbiased training data for AI models", "€20M or 4% turnover")
]

cursor.executemany("""
INSERT INTO EU_Regulations (regulation_article, framework, effective_date, department_impacted, key_focus, penalty_range)
VALUES (?, ?, ?, ?, ?, ?);
""", regulations_data)

connection.commit()

# Step 4: Compliance Alerts
print("\n🔔 Compliance Alerts:")

# Alert 1: Penalties above €20M
cursor.execute("SELECT regulation_article, penalty_range FROM EU_Regulations WHERE penalty_range LIKE '%35M%' OR penalty_range LIKE '%7% turnover%';")
high_penalties = cursor.fetchall()
for reg in high_penalties:
    print(f"⚠️ High Penalty Risk: {reg[0]} → {reg[1]}")

# Alert 2: Upcoming deadlines within 60 days
today = datetime.today()
cursor.execute("SELECT regulation_article, effective_date FROM EU_Regulations WHERE effective_date NOT LIKE 'Ongoing';")
deadlines = cursor.fetchall()
for reg in deadlines:
    effective_date = datetime.strptime(reg[1], "%Y-%m-%d")
    days_left = (effective_date - today).days
    if 0 < days_left <= 60:
        print(f"📅 Upcoming Deadline: {reg[0]} → {reg[1]} ({days_left} days left)")

connection.close()
