from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/items", tags=["items"])

class Item(BaseModel):
    name: str
    price: float

@router.get("/")
def list_items():
    return [
        {"id": 1, "name": "Book", "price": 19.99},
        {"id": 2, "name": "Pen", "price": 1.99}
]

@router.get("/{item_id}")
def read_item(item_id: int):
    if item_id > 100:
        raise HTTPException(status_code=404, detail = "Item not found")
    return {"item_id": item_id}

@router.post("/")
def create_item(item: Item):
    return {"message": "Iten created", "name": item.name, "price": item.price}
