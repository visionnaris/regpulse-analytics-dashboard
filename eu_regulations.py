import sqlite3

# Step 1: Connect to (or create) the SQLite database
connection = sqlite3.connect("EU_Regulations.db")
cursor = connection.cursor()

# Step 2: Create the EU_Regulations table
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

# Step 3: Define the regulatory data
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

# Step 4: Insert the data into the table
cursor.executemany("""
INSERT INTO EU_Regulations (regulation_article, framework, effective_date, department_impacted, key_focus, penalty_range)
VALUES (?, ?, ?, ?, ?, ?);
""", regulations_data)
print("✅ EU_Regulations database created and populated successfully!")

# Step 5: Commit changes and close the connection
connection.commit()

conn = sqlite3.connect("EU_Regulations.db")
cur = conn.cursor()
cur.execute("SELECT * FROM EU_Regulations;")
for row in cur.fetchall():
    print(row)

print("✅ EU_Regulations data verified successfully!")

conn.close()
connection.close()


