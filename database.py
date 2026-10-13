import sqlite3

# Connect to the database (creates it if it doesn't exist)
connection = sqlite3.connect("school.db")
cursor = connection.cursor()

# Start fresh each run (for learning only — never do this in production)
cursor.execute("DROP TABLE IF EXISTS students")

# Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT NOT NULL
)
""")

# Insert multiple students using executemany
cursor.executemany(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
    [
        ("cia", 18, "A"),
        ("dia", 19, "B"),
        ("eia", 20, "C")
    ]
)
connection.commit()

# Query 1: All students
print("All students:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Query 2: Students older than 18
print("\nStudents older than 18:")
cursor.execute("SELECT * FROM students WHERE age > ?", (18,))
for row in cursor.fetchall():
    print(row)

# Query 3: Students with grade A
print("\nStudents with grade A:")
cursor.execute("SELECT * FROM students WHERE grade = ?", ("A",))
for row in cursor.fetchall():
    print(row)

# Update: change eia's grade to A
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", ("A", "eia"))
connection.commit()

print("\nAfter updating eia's grade to A:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Delete: remove dia
cursor.execute("DELETE FROM students WHERE name = ?", ("dia",))
connection.commit()

print("\nAfter deleting dia:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Close the connection
connection.close()
