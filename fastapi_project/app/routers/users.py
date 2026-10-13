from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

class Address(BaseModel):
    city: str
    country: str

class User(BaseModel):
    name: str
    age: int
    address: Address

@router.get("/")
def list_users():
    return [
        {"id": 1, "name": "CiA", "age": 18},
        {"id": 2, "name": "Cia", "age": 19}
    ]

@router.get("/{user_id}")
def read_user(user_id: int):
    return {"user:id": user_id}

@router.post("/")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "city": user.address.city,
        "country": user.address.counrty 
    }
