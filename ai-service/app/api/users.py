from fastapi import APIRouter, Depends, HTTPException, status
from app.models.schemas import UserCreate, UserLogin, UserOut, Token
from app.utils.security import hash_password, verify_password, create_access_token
from app.services.db import db
from app.services.auth import get_current_user

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=201)
async def register(user: UserCreate):
    async with db.pool.acquire() as conn:
        existing = await conn.fetchrow("SELECT id FROM users WHERE email=$1", user.email)
        if existing:
            raise HTTPException(400, "User already exists")
        hashed = hash_password(user.password)
        row = await conn.fetchrow(
            "INSERT INTO users (email, password_hash) VALUES ($1, $2) RETURNING id, email",
            user.email, hashed
        )
        return dict(row)

@router.post("/login", response_model=Token)
async def login(data: UserLogin):
    async with db.pool.acquire() as conn:
        user = await conn.fetchrow("SELECT * FROM users WHERE email=$1", data.email)
        if not user or not verify_password(data.password, user["password_hash"]):
            raise HTTPException(401, "Invalid credentials")
        token = create_access_token({"sub": user["email"]})
        return {"access_token": token, "token_type": "bearer"}

@router.get("/profile", response_model=UserOut)
async def profile(current_user=Depends(get_current_user)):
    return current_user
