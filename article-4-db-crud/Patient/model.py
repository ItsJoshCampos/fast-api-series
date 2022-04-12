from sqlalchemy import Column, Integer, String, DateTime
from utils.connection import Base

class Patient(Base):
    __tablename__ = 'Patient'

    ID = Column(Integer, primary_key=True)
    BirthDate = Column(DateTime)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    AccountNumber = Column(String(25))
    Department = Column(String(20))
    Room = Column(String(1))

