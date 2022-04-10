from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    

class TrainExperiment(Base):
    __tablename__ = "experiment"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    model_id=Column(Integer,index=True)
    # model_name = Column(String(32),index=True)
    train_params = Column(String(256))
