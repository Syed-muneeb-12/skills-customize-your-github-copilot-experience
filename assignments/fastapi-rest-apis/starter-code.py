from typing import Optional, List
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = Field(..., example=1)
    name: str = Field(..., example="Widget")
    description: Optional[str] = Field(None, example="A useful widget")
    price: float = Field(..., gt=0, example=9.99)
    tags: List[str] = []

app = FastAPI(title="Starter API - FastAPI Assignment")

# simple in-memory storage
DB: List[dict] = []

def check_token(x_token: Optional[str] = Header(None)):
    if x_token != "secrettoken":
        raise HTTPException(status_code=401, detail="Invalid or missing X-Token header")


@app.post("/items/", response_model=Item)
def create_item(item: Item):
    if any(i["id"] == item.id for i in DB):
        raise HTTPException(status_code=400, detail="Item ID already exists")
    DB.append(item.dict())
    return item


@app.get("/items/", response_model=List[Item])
def list_items(skip: int = 0, limit: int = 10, q: Optional[str] = None):
    results = DB
    if q:
        results = [r for r in results if q.lower() in r.get("name", "").lower()]
    return results[skip : skip + limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for r in DB:
        if r["id"] == item_id:
            return r
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for idx, r in enumerate(DB):
        if r["id"] == item_id:
            DB[idx] = item.dict()
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, r in enumerate(DB):
        if r["id"] == item_id:
            DB.pop(idx)
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/admin/secure-action", dependencies=[Depends(check_token)])
def secure_action():
    return {"ok": True, "msg": "Authorized"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
