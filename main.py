from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
floor = 1.0


class Item(BaseModel):
    username: str
    price: float
    item_name: str


@app.get("/")
async def root():
    return "Hello World"


@app.get("/items")
async def items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.post("/discount")
async def discount(item: Item):
    if item.price * 0.8 < floor:
        raise HTTPException(status_code=400, detail="It is impossible to apply a discount for this product, the price "
                                                    "of a discounted product cannot be lower than 1 $")
    item.price *= 0.8
    item.item_name += " (Discount)"
    return item

