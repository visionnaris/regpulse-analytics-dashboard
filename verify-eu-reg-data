import sqlite3

conn = sqlite3.connect("EU_Regulations.db")
cur = conn.cursor()
cur.execute("SELECT * FROM EU_Regulations;")
for row in cur.fetchall():
    print(row)
conn.close()
