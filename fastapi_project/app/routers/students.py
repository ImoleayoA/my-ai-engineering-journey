from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db import get_db
from app.models import Student as StudentModel

router = APIRouter(prefix="/students", tags=["students"])

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str

class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    grade: str

    class Config:
        from_attributes = True

@router.get("/", response_model=list[StudentResponse])
def list_students(db: Session = Depends(get_db)):
    return db.query(StudentModel).all()

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session =  Depends(get_db)):
    student = db.get(StudentModel, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.post("/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = StudentModel(
        name=student.name,
        age=student.age,
        grade=student.grade
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.get(StudentModel, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db_student.name = student.name
    db_student.age = student.age
    db_student.grade = student.grade
    db.commit()
    db.refresh(db_student)
    return db_student

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.get(StudentModel, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted"}
