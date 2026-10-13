from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import get_connection

router = APIRouter(prefix="/students", tags=["students"])

class Student(BaseModel):
    name: str
    age: int
    grade: str

@router.get("/")
def list_students():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    connection.close()
    return [dict(row) for row in rows]

@router.get("/{student_id}")
def get_student(student_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return dict(row)

@router.post("/")
def create_student(student: Student):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        (student.name, student.age, student.grade)
    )
    connection.commit()
    new_id = cursor.lastrowid
    connection.close()
    return {"id": new_id, "name": student.name, "age": student.age, "grade": student.grade}

@router.put("/{student_id}")
def update_student(student_id: int, student: Student):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if cursor.fetchone() is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Student not found")
    cursor.execute(
        "UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?", (student.name, student.age, student.grade, student_id)
    )
    connection.commit()
    connection.close()
    return {"id": student_id, "name": student.name, "age": student.age, "grade": student.grade}

@router.delete("/{student_id}")
def delete_student(student_id: int):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    if cursor.fetchone() is None:
        connection.close()
        raise HTTPException(status_code=404, detail="Student not found")
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    connection.commit()
    connection.close()
    return {"message": "Student deleted"}
