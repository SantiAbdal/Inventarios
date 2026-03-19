from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from schemas.user_schema import Token, UserCreate
from sqlalchemy.orm import Session
from repository.user_repository import UserRepository
from core.security import hash_password, verify_password , create_access_token, decode_access_token

class AuthService:
   

    def register_user(self, db: Session, user_data: UserCreate):
        repo = UserRepository(db)
        if repo.get_by_email(user_data.email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        if repo.get_by_user_name(user_data.user_name):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
        if not user_data.user_name or not user_data.email or not user_data.password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username, email, and password are required")
        if len(user_data.password) < 5:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must be at least 6 characters long")
        
        hashed = hash_password(user_data.password)
        return repo.create(user_data, hashed)
    
    def login_user(self, db: Session, user_name: str, password: str) -> Token:
        repo = UserRepository(db)
        user = repo.get_by_user_name(user_name)
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        token = create_access_token({"sub": user.id})
        return Token(access_token=token, token_type="bearer")