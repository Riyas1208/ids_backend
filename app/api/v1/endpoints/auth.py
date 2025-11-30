from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.security import create_jwt

router = APIRouter()

users_db = {}  # simple in-memory store

class RegisterIn(BaseModel):
    username: str
    password: str

class LoginIn(BaseModel):
    username: str
    password: str


@router.post('/register')
def register(payload: RegisterIn):
    if payload.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    # store user
    users_db[payload.username] = {
        "username": payload.username,
        "password": payload.password,  # plaintext → can add hashing later
    }

    return {"message": "User registered successfully"}


@router.post('/login')
def login(payload: LoginIn):
    user = users_db.get(payload.username)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user["password"] != payload.password:
        raise HTTPException(status_code=401, detail="Invalid password")

    token = create_jwt(payload.username, expires_minutes=360)
    return {"access_token": token}
