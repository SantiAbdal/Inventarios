from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.db import Base
from sqlalchemy import Enum as SQLEnum
from schemas.user_state_schema import UserState

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    state = Column(SQLEnum(UserState), nullable=False)