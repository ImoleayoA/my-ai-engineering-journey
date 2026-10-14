from fastapi import FastAPI
from app.db import init_db
from app.routers import items, users, students, documents

app = FastAPI(title="My FastAPI Project")

init_db()

app.include_router(items.router)
app.include_router(users.router)
app.include_router(students.router)
app.include_router(documents.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}
