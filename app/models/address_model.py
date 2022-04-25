from sqlalchemy import Column, Integer, String
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref

@dataclass
class AddressModel(db.Model):
    
    id: int
    street: str
    number: int
    zip_code: str
    district: str

    __tablename__= "adresses"
    
    id = Column(Integer, primary_key=True)
    street = Column(String)
    number = Column(Integer)
    zip_code = Column(String)
    district = Column(String)
    
    establishment = relationship(
        "EstablishmentModel",
        backref=backref("establishments", uselist=False),
        uselist=False
        )


