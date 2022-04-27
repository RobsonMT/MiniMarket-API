from dataclasses import dataclass
from datetime import datetime as dt
from email.policy import default

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import backref, relationship

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
    establishments: list

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    avatar = Column(String)
    created = Column(DateTime, default=dt.now())
    last_access = Column(DateTime, default=dt.now())
    is_activate = Column(Boolean, default=True)

    establishments = relationship(
        "EstablishmentModel",
        backref=backref("establishment", uselist=False),
        uselist=True,
    )
