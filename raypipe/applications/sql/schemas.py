from typing import Optional

from pydantic import BaseModel, validator
from datetime import datetime


class Algorithm(BaseModel):
    id:Optional[int]
    model_name:str
    create_time: datetime = None
    update_time: datetime = None

    @validator('create_time', pre=True, always=True)
    def set_create_now(cls, v):
        return v or datetime.now()

    @validator('update_time', pre=True, always=True)
    def set_update_now(cls, v):
        return v or datetime.now()


class TrainExperiment(BaseModel):
    id:Optional[int]
    algorithm_id:int
    train_params:str
    create_time: datetime = None
    update_time: datetime = None

    @validator('create_time', pre=True, always=True)
    def set_create_now(cls, v):
        return v or datetime.now()

    @validator('update_time', pre=True, always=True)
    def set_update_now(cls, v):
        return v or datetime.now()


class Model(BaseModel):
    id:Optional[int]
    exp_id:int
    save_path:str
    create_time: datetime = None
    update_time: datetime = None

    @validator('create_time', pre=True, always=True)
    def set_create_now(cls, v):
        return v or datetime.now()

    @validator('update_time', pre=True, always=True)
    def set_update_now(cls, v):
        return v or datetime.now()
