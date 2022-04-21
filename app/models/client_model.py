from sqlalchemy import Column, Boolean, ForeignKey, Integer, String, DateTime
from datetime import date 
from dataclasses import dataclass

@dataclass
class ClientModel:
    
    id: int
    name: str
    avatar: str
    contact: str
    pay_date: date
    is_dobtor: bool
    is_late: bool
    is_activate: bool
    estabilishment_id: int

    __tablename__= "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=True)
    avatar = Column(String)
    contact = Column(String, unique=True, nullable=True)
    pay_date = Column(DateTime, nullable=True)
    is_dobtor = Column(Boolean, nullable=True)
    is_late = Column(Boolean, nullable=True)
    is_activate = Column(Boolean, nullable=True)
    estabilishment_id = Column(Integer,ForeignKey("establishments.id"))