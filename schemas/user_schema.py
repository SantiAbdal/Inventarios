from pydantic import BaseModel, ConfigDict
from schemas.user_state_schema import UserState
# User Schemas
class UserBase(BaseModel):
    user_name: str
    email: str
    password: str
    state: UserState

class UserCreate(UserBase):
    pass

class UserResponse(BaseModel):
    id: int
    user_name: str
    email: str
    state: UserState
    
    model_config = ConfigDict(from_attributes=True)
    
class UserUpdate(BaseModel):
    user_name: str | None = None
    state: UserState | None = None

# Token Schemas
class Token(BaseModel):
    access_token: str
    token_type: str