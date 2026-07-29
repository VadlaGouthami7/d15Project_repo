from sqlalchemy.orm import Session
import model
import schemas
#CREATE(POST)
#create for electronics
def create_electronic(db: Session, electronic: schemas.ElectronicsCreate):
    db_electronic= model.Electronics(**electronic.model_dump())  #creating a new electronic record
    db.add(db_electronic) #adding the electronic to existing table
    db.commit()  # committing the changes to db
    db.refresh(db_electronic)  #refreshing to fetch the updated table
    return db_electronic  #sending the response to user

#create for footwear
def create_footwear(db: Session, footwear: schemas.FootwearCreate):
    db_footwear= model.FootWear(**footwear.model_dump())  #creating a new footwear record
    db.add(db_footwear) #adding the footwear to existing table
    db.commit()  # committing the changes to db
    db.refresh(db_footwear)  #refreshing to fetch the updated table
    return db_footwear

# GET
# get by category

#for electronics:
def get_electronics(db: Session):
    return db.query(model.Electronics).all()
# for footwear
def get_footwears(db: Session):
    return db.query(model.FootWear).all()


#get by category id
#for electronics:
def get_electronic(db: Session, electronic_id: int):
    return db.query(model.Electronics).filter(
        model.Electronics.id == electronic_id
    ).first()
# for footwear:
def get_footwear(db: Session, footwear_id: int):
    return db.query(model.FootWear).filter(
        model.FootWear.f_id == footwear_id
    ).first()




#UPDATE 
#for electronics
def update_electronic(db: Session, electrnic_id: int, electronic: schemas.ElectronicsCreate):
    db_electronic = get_electronic(db, electrnic_id)
    if not db_electronic:
        return None
    db_electronic.name = electronic.name
    db_electronic.e_type = electronic.e_type
    db_electronic.price = electronic.price
    db_electronic.voltage=electronic.voltage
    db.commit()
    db.refresh(db_electronic)
    return db_electronic

#for footwear
def update_footwear(db: Session, FW_id: int, footwear: schemas.FootwearCreate):
    db_footwear = get_footwear(db, FW_id)
    if not db_footwear:
        return None
    db_footwear.f_name = footwear.f_name
    db_footwear.f_price = footwear.f_price
    db_footwear.company= footwear.company
    
    db.commit()
    db.refresh(db_footwear)
    return db_footwear

# DELETE
#for electronics
def delete_electronic(db: Session, electronic_id: int):
    db_electronic =get_electronic(db, electronic_id)
    if not db_electronic:
        return None
    db.delete(db_electronic)
    db.commit()
    return db_electronic
#for footwear
def delete_footwear(db: Session, foot_id: int):
    db_footwear =get_footwear(db, foot_id)
    if not db_footwear:
        return None
    db.delete(db_footwear)
    db.commit()
    return db_footwear
