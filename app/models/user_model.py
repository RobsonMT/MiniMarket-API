from dataclasses import dataclass
from datetime import datetime as dt

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import backref, relationship
from werkzeug.security import check_password_hash, generate_password_hash

from app.configs.database import db


@dataclass
class UserModel(db.Model):

    id: int
    name: str
    email: str
    contact: str
    password_hash: str
    avatar: str
    created: dt
    last_access: dt
    is_activate: bool
    establishment: list

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    contact = Column(String(100), nullable=False)
    password_hash = Column(String, nullable=False)
    avatar = Column(String)
    created = Column(DateTime, default=dt.now())
    last_access = Column(DateTime, default=dt.now())
    is_activate = Column(Boolean, default=True)

    establishment = relationship(
        "EstablishmentModel",
        backref=backref("owner", uselist=False),
        uselist=True,
    )

    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def verify_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
