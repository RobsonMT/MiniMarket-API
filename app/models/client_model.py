from dataclasses import dataclass
from email.policy import default

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from app.configs.database import db


@dataclass
class ClientModel(db.Model):

    id: int
    name: str
    avatar: str
    contact: str
    pay_day: int
    is_dobtor: bool
    is_late: bool
    is_activate: bool
    establishment_id: int

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    avatar = Column(String)
    contact = Column(String, nullable=False, unique=True)
    pay_day = Column(Integer, nullable=False)
    is_dobtor = Column(Boolean, nullable=False, default=False)
    is_late = Column(Boolean, nullable=False, default=False)
    is_activate = Column(Boolean, nullable=False, default=True)
    establishment_id = Column(Integer, ForeignKey("establishments.id"), nullable=False)

    sales = relationship(
        "SaleModel", backref=backref("clients", uselist=True), uselist=False
    )
