import datetime

from sqlalchemy import Boolean, Column, Integer, String,DateTime
from .database import Base


class Algorithm(Base):
    __tablename__ = "algorithm"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    model_name = Column(String(32),index=True)
    create_time=Column("create_time",DateTime,index=False, nullable=False,default=datetime.datetime.utcnow)
    update_time = Column("update_time", DateTime, index=False, nullable=False, default=datetime.datetime.utcnow)


class TrainExperiment(Base):
    __tablename__ = "experiment"
    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    algorithm_id=Column(Integer,index=True)
    train_params = Column(String(256))
    create_time=Column("create_time",DateTime,index=False, nullable=False,default=datetime.datetime.utcnow)
    update_time = Column("update_time", DateTime, index=False, nullable=False, default=datetime.datetime.utcnow)

class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    exp_id = Column(Integer, index=True)
    save_path=Column(String(256))
    create_time=Column("create_time",DateTime,index=False, nullable=False,default=datetime.datetime.utcnow)
    update_time = Column("update_time", DateTime, index=False, nullable=False, default=datetime.datetime.utcnow)
