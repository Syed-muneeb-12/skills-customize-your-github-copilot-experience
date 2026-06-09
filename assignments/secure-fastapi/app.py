from typing import Optional, List
from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel, Field
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "data.db"

def get_db_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

class ItemIn(BaseModel):
    name: str = Field(..., example="Widget")
    description: Optional[str] = Field(None, example="A useful widget")
    price: float = Field(..., gt=0, example=9.99)

class ItemOut(ItemIn):
    id: int

app = FastAPI(title="Secure Persistent FastAPI")

def init_db():
    conn = get_db_conn()
    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                price REAL NOT NULL
            )
            """
        )
    conn.close()


def check_token(x_token: Optional[str] = Header(None)):
    if x_token != "secrettoken":
        raise HTTPException(status_code=401, detail="Invalid or missing X-Token header")


@app.on_event("startup")
def startup():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    init_db()


@app.post("/items/", response_model=ItemOut)
def create_item(item: ItemIn):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
                (item.name, item.description, item.price))
    conn.commit()
    item_id = cur.lastrowid
    conn.close()
    return ItemOut(id=item_id, **item.dict())


@app.get("/items/", response_model=List[ItemOut])
def list_items(skip: int = 0, limit: int = 10, q: Optional[str] = None):
    conn = get_db_conn()
    sql = "SELECT id, name, description, price FROM items"
    params: List = []
    if q:
        sql += " WHERE name LIKE ?"
        params.append(f"%{q}%")
    sql += " ORDER BY id LIMIT ? OFFSET ?"
    params.extend([limit, skip])
    cur = conn.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return [ItemOut(**dict(r)) for r in rows]


@app.get("/items/{item_id}", response_model=ItemOut)
def get_item(item_id: int):
    conn = get_db_conn()
    cur = conn.execute("SELECT id, name, description, price FROM items WHERE id = ?", (item_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemOut(**dict(row))


@app.put("/items/{item_id}", response_model=ItemOut)
def update_item(item_id: int, item: ItemIn):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?",
                (item.name, item.description, item.price, item_id))
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.commit()
    conn.close()
    return ItemOut(id=item_id, **item.dict())


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM items WHERE id = ?", (item_id,))
    if cur.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.commit()
    conn.close()
    return {"ok": True}


@app.post("/admin/secure-action", dependencies=[Depends(check_token)])
def secure_action():
    return {"ok": True, "msg": "Authorized"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
