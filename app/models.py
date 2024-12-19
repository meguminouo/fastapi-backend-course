from sqlalchemy import Column, Date, Integer, String, Boolean, Enum
from .database import Base
import enum

# Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

class UserStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETED = "deleted"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)  # 字串類型，限制長度為50，必填，且必須唯一
    password = Column(String(255), nullable=False)  # 字串類型，設為255長度以容納加密密碼，必填
    email = Column(String(255), unique=True, nullable=False)  # 字串類型，設為255長度，必填，且必須唯一
    status = Column(Enum(UserStatus), default=UserStatus.ACTIVE, nullable=False)  # 使用Enum定義狀態，預設值為ACTIVE
