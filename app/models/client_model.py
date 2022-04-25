from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, DateTime
from datetime import date
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
@dataclass
class ClientModel(db.Model):
    
    id: int
    name: str
    avatar: str
    contact: str
    estabilishment_id: int
    pay_day: int
    is_dobtor: bool
    is_late: bool
    is_activate: bool
    
    __tablename__= "clients"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=True)
    avatar = Column(String)
    contact = Column(String, unique=True, nullable=True)
    estabilishment_id = Column(Integer, ForeignKey("establishments.id"))
    pay_day = Column(Integer, nullable=True)
    is_dobtor = Column(Boolean, nullable=True, default=False)
    is_late = Column(Boolean, nullable=True, default=False)
    is_activate = Column(Boolean, default=True, nullable=True)

    sales = relationship(
        "SaleModel",
        backref=backref("sales", uselist=True),
        uselist=False
    )


