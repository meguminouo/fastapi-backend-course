from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    descripton: str = None

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/items/")
def create_item(item: Item):
    print(f"Received item: {item}")
    return {"massage":"Item received","item":item}