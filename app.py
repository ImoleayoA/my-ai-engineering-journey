from fastapi import FastAPI, Query, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


class Address(BaseModel):
    city: str
    country: str


class User(BaseModel):
    name: str
    age: int
    address: Address


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/about")
def read_about():
    return {"name": "CiA", "goal": "AI Engineer"}


@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., ge=1)):
    if item_id > 100:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}


@app.get("/search")
def read_search(
    q: str = Query("", min_length=2, max_length=50),
    limit: int = Query(10, ge=1, le=100)
):
    return {"query": q, "limit": limit}


@app.post("/items")
def create_item(item: Item):
    return {
        "message": "Item created",
        "name": item.name,
        "price": item.price
    }


@app.get("/users/{user_id}/posts/{post_id}")
def read_user_post(user_id: int, post_id: int):
    return {"user_id": user_id, "post_id": post_id}


@app.post("/users")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "city": user.address.city,
        "country": user.address.country
    }
