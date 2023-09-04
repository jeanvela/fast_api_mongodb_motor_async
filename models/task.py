from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId  #* Compruba si el id que estamos pasando luce como un id de mongodb

#* Trabajando con motor
# class PyObjectId(ObjectId):
#     @classmethod
#     def __get_validators__(cls):
#         yield cls.validate
    
#     @classmethod
#     def validate(cls, v):
#         if not ObjectId.is_valid(v):
#             raise ValueError('Invalid objectid')
#         return str(v)

class Task(BaseModel):
    # id: Optional[str] = Field(alias='_id', default=None) #* No es un dato cualquiera sino que va a inicializarlo con un alias _id
    title: str
    description: str
    completed: bool = False
    
    # class Config:
        # arbitrary_types_allowed = True
    # class Config:
    #     from_attributes = True  #* Los campos de la misma clase pueden ser tratados dentro del mismo modulo
    #     populate_by_name = True  #* Para convertir los campos que inicialmente esten adentro
    #     json_encoders = {ObjectId: str}
        
        
class updateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    
    class Config:
        from_attributes = True  #* Los campos de la misma clase pueden ser tratados dentro del mismo modulo
        populate_by_name = True  #* Para convertir los campos que inicialmente esten adentro
        json_encoders = {ObjectId: str}