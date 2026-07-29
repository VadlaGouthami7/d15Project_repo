from pydantic import BaseModel

class ElectronicsCreate(BaseModel):
    name :str 
    e_type :str 
    price:int
    voltage:str

class electronicsResponse(ElectronicsCreate):
    id: int

    model_config = {
        "from_attributes": True
    }



# TABLE_2
class FootwearCreate(BaseModel):
    f_name:str
    size:int
    f_price :int
    company:str

class FootwearResponse(FootwearCreate):
    f_id: int

    model_config = {
        "from_attributes": True
    }
