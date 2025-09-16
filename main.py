from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# FastAPI instance
app = FastAPI()

# Data model
class Item(BaseModel):
    id: int
    name: str
    price: float
    is_offer: bool = None

# Fake in-memory database
items_db: List[Item] = []

# -------------------- CRUD Operations --------------------

# CREATE (POST)
@app.post("/items/", response_model=Item , tags=["Items"])
def create_item(item: Item):
    # check duplicate id
    for existing_item in items_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items_db.append(item)
    return item

# READ ALL (GET)
@app.get("/items/", response_model=List[Item] , tags = ["Items"])
def get_items():
    return items_db

# READ ONE (GET by ID)
@app.get("/items/{item_id}", response_model=Item , tags = ["Items"])
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# UPDATE (PUT)
@app.put("/items/{item_id}", response_model=Item , tags = ["Items"])
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE (DELETE)
@app.delete("/items/{item_id}" , tags = ["Items"])
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"message": f"Item {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
