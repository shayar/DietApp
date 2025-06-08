import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_crud_items(monkeypatch):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Register & login
        await ac.post("/users/register", json={"email": "itemuser@example.com", "password": "pass"})
        r = await ac.post("/users/login", json={"email": "itemuser@example.com", "password": "pass"})
        token = r.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        # Create
        r = await ac.post("/items/", json={"title": "My Item"}, headers=headers)
        assert r.status_code == 201
        item_id = r.json()["id"]
        # Read
        r = await ac.get(f"/items/{item_id}", headers=headers)
        assert r.status_code == 200
        # Update
        r = await ac.put(f"/items/{item_id}", json={"description": "Updated"}, headers=headers)
        assert r.status_code == 200
        # List
        r = await ac.get("/items/", headers=headers)
        assert r.status_code == 200
        assert isinstance(r.json(), list)
        # Delete
        r = await ac.delete(f"/items/{item_id}", headers=headers)
        assert r.status_code == 204
