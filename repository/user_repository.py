from sqlalchemy.orm import Session
from models.user_model import UserModel
from schemas.user_schema import UserCreate

class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, user_data: UserCreate, hashed_password: str) -> UserModel:
        user = UserModel(
            user_name=user_data.user_name,
            email=user_data.email,
            password_hash=hashed_password,
            state=user_data.state
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user_id: int) -> bool:
        user = self.get_by_id(user_id)
        if not user:
            return False

        self.db.delete(user)
        self.db.commit()
        return True

    def get_by_email(self, email: str) -> UserModel | None:
        return (
            self.db.query(UserModel)
            .filter(UserModel.email == email)
            .first()
        )
    
    def get_by_user_name(self, username: str) -> UserModel | None:
        return (
            self.db.query(UserModel)
            .filter(UserModel.user_name == username)
            .first()
        )
    
    def get_by_id(self, user_id: int) -> UserModel | None:
        return (
            self.db.query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )
    