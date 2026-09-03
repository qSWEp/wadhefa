import sqlite3

connection = sqlite3.connect("wadhefa.db")
cursor = connection.cursor()

cursor.execute("SELECT id, title, company, status FROM jobs")
rows = cursor.fetchall()
print(f"total job {len(rows)}")   
for row in rows:
    print(f"[{row[0]}] {row[1]} — {row[2]} {row[3]}")


connection.close()
   
