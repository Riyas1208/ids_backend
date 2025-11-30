from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import create_jwt

router = APIRouter()

class LoginIn(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(payload: LoginIn):
    # PLACEHOLDER: replace with real user check
    if payload.username == 'admin' and payload.password == 'admin':
        token = create_jwt(payload.username, expires_minutes=360)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail='Invalid credentials')
