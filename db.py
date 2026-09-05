import sqlite3

connection = sqlite3.connect("wadhefa.db")
cursor = connection.cursor()

cursor.execute("UPDATE jobs SET status = ? WHERE id = ?",("applied", 1))

if cursor.rowcount == 0:
    print("No rows were updated.")
else:
    print(f"{cursor.rowcount} row(s) were updated.")

connection.commit()

cursor.execute("SELECT id , title, status FROM jobs")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: [{row[0]}]   Title: {row[1]}  Status: {row[2]}")
connection.close()
   
