from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.models.schemas import ItemCreate, ItemUpdate, ItemOut
from app.services.db import db
from app.services.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=ItemOut, status_code=201)
async def create_item(item: ItemCreate, user=Depends(get_current_user)):
    async with db.pool.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO items (title, description, owner_id) VALUES ($1, $2, $3) RETURNING id, title, description, owner_id",
            item.title, item.description, user["id"]
        )
        return dict(row)

@router.get("/", response_model=List[ItemOut])
async def list_items(user=Depends(get_current_user)):
    async with db.pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT id, title, description, owner_id FROM items WHERE owner_id=$1",
            user["id"]
        )
        return [dict(row) for row in rows]

@router.get("/{item_id}", response_model=ItemOut)
async def get_item(item_id: int, user=Depends(get_current_user)):
    async with db.pool.acquire() as conn:
        row = await conn.fetchrow(
            "SELECT id, title, description, owner_id FROM items WHERE id=$1 AND owner_id=$2",
            item_id, user["id"]
        )
        if not row:
            raise HTTPException(404, "Item not found")
        return dict(row)

@router.put("/{item_id}", response_model=ItemOut)
async def update_item(item_id: int, item: ItemUpdate, user=Depends(get_current_user)):
    async with db.pool.acquire() as conn:
        row = await conn.fetchrow(
            "UPDATE items SET title=COALESCE($1,title), description=COALESCE($2,description) WHERE id=$3 AND owner_id=$4 RETURNING id, title, description, owner_id",
            item.title, item.description, item_id, user["id"]
        )
        if not row:
            raise HTTPException(404, "Item not found")
        return dict(row)

@router.delete("/{item_id}", status_code=204)
async def delete_item(item_id: int, user=Depends(get_current_user)):
    async with db.pool.acquire() as conn:
        result = await conn.execute(
            "DELETE FROM items WHERE id=$1 AND owner_id=$2",
            item_id, user["id"]
        )
        if result == "DELETE 0":
            raise HTTPException(404, "Item not found")
        return
    {"detail": "Item deleted successfully"}