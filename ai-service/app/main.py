from fastapi import FastAPI
from app.api import users, items
from app.services.db import db

app = FastAPI(
    title="AI Project Python API",
    description="A FastAPI application for managing users and items in an AI based Diet App project.",
    version="1.0.0"
)

@app.on_event("startup")
async def on_startup():
    await db.connect()

@app.on_event("shutdown")
async def on_shutdown():
    await db.close()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
