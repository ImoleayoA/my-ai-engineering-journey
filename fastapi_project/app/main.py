from fastapi import FastAPI
from app.routers import items, users 

app = FastAPI(title="My FastAPI Project")

app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}
