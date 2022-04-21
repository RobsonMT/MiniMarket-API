from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime as dt
from app.configs.database import db
@dataclass
class UserModel(db.Model):
    
    id: int
    name: str
    email: str
    contact: str
    password: str
    avatar: str
    created: dt
    last_access: dt
    is_activate: bool

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100), unique=True)
    contact = Column(String(100))
    password = Column(String(100))
    avatar = Column(String)
    created = Column(DateTime)
    last_access = Column(DateTime)
    is_activate = Column(Boolean)