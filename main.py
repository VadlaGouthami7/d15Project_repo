from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#get for entire website(default)
@app.get("/")
def welcome():
    return "welcome to E-Commerce Portal! and at present we have product categories 1.electronic and 2.Footwear"


#POST OPERATION
# FOR ELECTRONICS
@app.post("/electronics", response_model=schemas.electronicsResponse)
def create(electronic: schemas.ElectronicsCreate, db: Session = Depends(get_db)):
    return crud.create_electronic(db, electronic)
#For FOOTWEAR
@app.post("/footwear", response_model=schemas.FootwearResponse)
def create(footwear: schemas.FootwearCreate, db: Session = Depends(get_db)):
    return crud.create_footwear(db, footwear)


#GET OPERATION FOR CATEGORY WISE
#FOR ELECTRONICS 
@app.get("/electronics", response_model=list[schemas.electronicsResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_electronics(db)
#FOR FOOTWEAR
@app.get("/footwear", response_model=list[schemas.FootwearResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_footwears(db)


#get CATEGORY by id
#for electronics
@app.get("/electronics/{electronic_id}", response_model=schemas.electronicsResponse)
def read_one(electronic_id: int, db: Session = Depends(get_db)):
    electronic = crud.get_electronic(db, electronic_id)
    if not electronic:
        raise HTTPException(status_code=404, detail=f"electronic with given id {electronic_id} ,not found")
    return electronic
# for footwear
@app.get("/footwear/{fw_id}", response_model=schemas.FootwearResponse)
def read_one(fw_id: int, db: Session = Depends(get_db)):
    footwear = crud.get_footwear(db, fw_id)
    if not footwear:
        raise HTTPException(status_code=404, detail=f"footwear with given id {fw_id},not found")
    return footwear


#PUT OPERATION
#FOR ELECTRONICS
@app.put("/electronics/{e_id}", response_model=schemas.electronicsResponse)
def update(e_id: int, electronic: schemas.ElectronicsCreate, db: Session = Depends(get_db)):
    updated_e = crud.update_electronic(db, e_id, electronic)
    if not updated_e:
        raise HTTPException(status_code=404, detail="electronic, which you want to update, not found")
    return updated_e
#For FOOTWEAR
@app.put("/footwear/{f_id}", response_model=schemas.FootwearResponse)
def update(f_id: int, footwear: schemas.FootwearCreate, db: Session = Depends(get_db)):
    updated_f = crud.update_footwear(db, f_id,footwear)
    if not updated_f:
        raise HTTPException(status_code=404, detail="Footwear, which you want to update, not found")
    return updated_f


#DELETE OPERATION
#for electronics
@app.delete("/electronics/{e_id}")
def delete(e_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_electronic(db, e_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"electronic with id {e_id} not found")
    return {"message":f"electronic with e_id {e_id},deleted successfully"}
#for footwear
@app.delete("/footwear/{f_id}")
def delete(f_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_footwear(db, f_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"footwear with id {f_id} not found")
    return {"message":f"footwear with f_id {f_id},deleted successfully"}
