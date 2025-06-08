from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.security import decode_access_token
from app.services.db import db

bearer_scheme = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    print("TOKEN RECEIVED:", token)
    try:
        payload = decode_access_token(token)
        print("PAYLOAD:", payload)
        email = payload.get("sub")
        if not email:
            print("NO EMAIL IN TOKEN")
            raise ValueError("No subject in token")
    except Exception as e:
        print("TOKEN DECODE ERROR", str(e))
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    async with db.pool.acquire() as conn:
        user = await conn.fetchrow("SELECT id, email FROM users WHERE email=$1", email)
        if not user:
            print("USER NOT FOUND FOR EMAIL:", email)
            raise HTTPException(status_code=404, detail="User not found")
        return dict(user)

