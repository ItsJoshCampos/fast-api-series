from datetime import datetime
from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class PatientCreate(BaseModel):
    BirthDate: datetime
    FirstName: str
    LastName: str
    AccountNumber: str
    Department: str
    Room: str

class Patient(BaseModel):
    ID: int
    BirthDate: datetime
    FirstName: str
    LastName: str
    AccountNumber: str
    Department: str
    Room: str

    # Orm Mode is used to support models that map to ORM objects, in this case model.Patient (sqlAlchemy)
    class Config:
        orm_mode = True

    
