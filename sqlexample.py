import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
)
""")

cursor.execute(
    "INSERT INTO users (name, email, age) VALUES (?,?,?)",
    ("CiA", "cia@example.com", 18)
)

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit()
connection.close()
