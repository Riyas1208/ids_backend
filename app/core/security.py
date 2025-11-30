from fastapi import Header, HTTPException, Depends
from typing import Optional
from app.core.config import settings
import jwt
from datetime import datetime, timedelta

def require_api_key(x_api_key: Optional[str] = Header(None)):
    if settings.IDS_API_KEY:
        if x_api_key != settings.IDS_API_KEY:
            raise HTTPException(status_code=401, detail="Invalid API key")
    return True

def create_jwt(subject: str, expires_minutes: int = 60):
    payload = {
        "sub": subject,
        "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)
    }
    token = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
    return token

def verify_jwt(token: str = Header(...)):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        return payload.get("sub")
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
