from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple REST API")

items = [
    {"id": 1, "name": "Notebook", "price": 3.5},
    {"id": 2, "name": "Pen", "price": 1.2}
]

class Item(BaseModel):
    id: int
    name: str
    price: float

@app.get("/")
def home():
    return {"message": "Simple REST API is running"}

@app.get("/items")
def get_items():
    return {"items": items}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}

@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return {"message": "Item added successfully", "item": item}