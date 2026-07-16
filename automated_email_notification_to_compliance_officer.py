import sqlite3
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
email_user = os.getenv("EMAIL_USER")
email_pass = os.getenv("EMAIL_PASS")

# Step 1: Connect to the database
connection = sqlite3.connect("EU_Regulations.db")
cursor = connection.cursor()

# Step 2: Fetch compliance alerts
alerts = []

# Penalty Alerts
cursor.execute("SELECT regulation_article, penalty_range FROM EU_Regulations WHERE penalty_range LIKE '%35M%' OR penalty_range LIKE '%7% turnover%';")
high_penalties = cursor.fetchall()
for reg in high_penalties:
    alerts.append(f"⚠️ High Penalty Risk: {reg[0]} → {reg[1]}")

# Deadline Alerts (within 60 days)
today = datetime.today()
cursor.execute("SELECT regulation_article, effective_date FROM EU_Regulations WHERE effective_date NOT LIKE 'Ongoing';")
deadlines = cursor.fetchall()
for reg in deadlines:
    effective_date = datetime.strptime(reg[1], "%Y-%m-%d")
    days_left = (effective_date - today).days
    if 0 < days_left <= 60:
        alerts.append(f"📅 Upcoming Deadline: {reg[0]} → {reg[1]} ({days_left} days left)")

connection.close()

# Step 3: Prepare email content
email_body = "\n".join(alerts) if alerts else "✅ No compliance alerts at this time."

msg = MIMEMultipart()
msg['From'] = "sonali.310162@gmail.com"
msg['To'] = "sonalisahu0512@gmail.com" #email_user #"compliance_officer@example.com"
msg['Subject'] = "EU Regulations Compliance Alerts - Deutsche Bank"

msg.attach(MIMEText(email_body, 'plain'))

# Step 4: Send email via SMTP
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Example: Gmail SMTP
    server.starttls()
    server.login("your_email@example.com", "your_password_or_app_password")
    server.send_message(msg)
    server.quit()
    print("📧 Compliance alert email sent successfully!")
except Exception as e:
    print(f"❌ Error sending email: {e}")
