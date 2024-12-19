from sqlalchemy import Column, Date, Integer, String, Boolean
from .database import Base

# Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

    priority = Column(Integer, default=1)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)  # 字串類型，限制長度為50，必填，且必須唯一
    password = Column(String(255), nullable=False)  # 字串類型，設為255長度以容納加密密碼，必填
    email = Column(String(255), unique=True, nullable=False)  # 字串類型，設為255長度，必填，且必須唯一

