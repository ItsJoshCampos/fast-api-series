from fastapi import FastAPI, Depends, HTTPException, status
from typing import List

import utils
from Patient import schema
from Patient import model
from sqlalchemy.orm import Session


app = FastAPI()


# CRUD Routes
# GET ALL
# Response will be a LIST of schema.Patient
# The Schema.Patient List instance will be mapped from the model.Patient ORM instance from Sql Alchemy
@app.get("/Patient", response_model=List[schema.Patient])
async def GetAll(db: Session = Depends(utils.get_db)):
    
    # get the model.patient with the given id
    # using sql alchemy orm, we're querying the Patient table
    query = db.query(model.Patient)
    patients = query.all()

    return patients
    

# GET Single
# Response will be a single schema.Patient 
# The Schema.Patient instance will be mapped from the model.Patient ORM instance from Sql Alchemy
@app.get("/Patient/{ID}")
async def GetSingle(ID: int, db: Session = Depends(utils.get_db)):
    
    # get the patient with the given Patient ID
    query = db.query(model.Patient).filter(model.Patient.ID == ID)
    patient = query.one_or_none()

    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient with ID {ID} not found")

    return patient

# POST
# Response will be a single schema.Patient after creation in the DB
# The Schema.Patient instance will be mapped from the model.Patient ORM instance from Sql Alchemy
@app.post("/Patient", response_model=schema.Patient)
async def Post(patient: schema.PatientCreate, db: Session = Depends(utils.get_db)):

    # create an instance of the model.Patient ORM model from the schema.Patient instance from the request body
    new_patient = model.Patient(BirthDate = patient.BirthDate
                            , FirstName = patient.FirstName
                            , LastName = patient.LastName
                            , AccountNumber = patient.AccountNumber
                            , Department = patient.Department
                            , Room = patient.Room)

    # add it to the session and commit it
    db.add(new_patient)
    db.commit()
    
    # update the patient instance to get the newly created Id
    db.refresh(new_patient) 

    # return the patient
    return new_patient

# PUT
# Response will be a single schema.Patient after creation in the DB
# The Schema.Patient instance will be mapped from the model.Patient ORM instance from Sql Alchemy
@app.put("/Patient/{ID}", response_model=schema.Patient)
async def Put(ID: int, patientUpdate: schema.Patient, db: Session = Depends(utils.get_db)):
    
    # get the model.Patient with the given id
    patient = db.get(model.Patient, ID)

    # update patient with the patient from request body (if patient with the given id was found)
    if patient:
        patient.BirthDate = patientUpdate.BirthDate
        patient.FirstName = patientUpdate.FirstName
        patient.LastName = patientUpdate.LastName
        patient.AccountNumber = patientUpdate.AccountNumber
        patient.Department = patientUpdate.Department
        patient.Room = patientUpdate.Room

        db.commit()
        db.refresh(patient)

    # check if patient with given id exists. If not, raise exception and return 404 not found response
    if not patient:
        raise HTTPException(status_code=404, detail=f"Patient with ID {ID} not found")

    return patient

# DELETE
@app.delete("/Patient/{ID}", status_code=status.HTTP_204_NO_CONTENT)
async def Delete(ID: int,  db: Session = Depends(utils.get_db)):
    
    # get the model.Patient with the given id
    patient = db.get(model.Patient, ID)

    # check if patient with given id exists and call delete
    if patient:
        db.delete(patient)
        db.commit()
