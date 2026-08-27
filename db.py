import sqlite3

connection = sqlite3.connect("wadhefa.db")
cursor = connection.cursor()

try:   
    cursor.execute(
        "INSERT INTO jobs (title, company, url) VALUES(?,?,?)",
        ("Software Engineer", "Tech Company", "https://techcompany.com/jobs/software-engineer")
    )
    print("Job inserted")

except sqlite3.IntegrityError:
    print("Job already exists in the data.")

connection.commit()
connection.close()
   
