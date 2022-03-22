from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator
from tortoise.contrib.pydantic import pydantic_model_creator, PydanticModel

from backend.core.app.models import User, Project, TeamMember

User_Pydantic = pydantic_model_creator(User, name="User")


class PasswordMixin(BaseModel):
    password: str = Field(...)

    @validator("password", pre=True)
    def validate_password(cls, value):
        if len(value) <= 8:
            raise ValueError("password must contain at least 8 characters")
        return value


class BaseUser(PydanticModel):
    email: EmailStr = Field(..., description="unique user email")
    first_name: str = Field(...)
    last_name: str = Field(...)


class UserCreate_Pydantic(BaseUser, PasswordMixin):
    """
    User creation schema
    """

    class Config:
        title = "UserCreate"


class ResetPassword(PasswordMixin):
    pass


Project_Pydantic = pydantic_model_creator(Project, name="Project")


class ProjectCreate(PydanticModel):
    name: str = Field(...)
    description: Optional[str]

    class Config:
        title = "ProjectCreate"


TeamMember_Pydantic = pydantic_model_creator(TeamMember, name="TeamMember")


class TeamMemberCreate(PydanticModel):
    user_id: int = Field(...)
    role: Optional[str]

    class Config:
        title = "TeamMemberCreate"


class ColumnCreate(PydanticModel):
    name: str = Field(...)

    class Config:
        title = "ColumnCreate"


class TaskCreate(PydanticModel):
    name: str = Field(...)
    description: Optional[str]

    class Config:
        title = "TaskCreate"


class TaskUpdate(TaskCreate):
    name: Optional[str]
    column_id: int = Field(...)

    class Config:
        title = "TaskUpdate"
