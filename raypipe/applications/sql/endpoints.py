from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine, Base
from .schemas import Algorithm, TrainExperiment, Model
from sqlalchemy.orm import Session
from . import crud

# Dependency
def get_db():
    """
    每一个请求处理完毕后会关闭当前连接，不同的请求使用不同的连接
    :return:
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_algorithms( db: Session = Depends(get_db)):
    return crud.get_algorithm(db=db)

def add_algorithm(algo: Algorithm, db: Session = Depends(get_db)):
    return crud.db_create_algo(db=db,algo=algo)

def get_experiment(exp_id:int,db: Session = Depends(get_db)):
    return crud.get_experiment(db=db, exp_id=exp_id)

def get_experiments( algo_id:int,db: Session = Depends(get_db)):
    return crud.get_all_experiments_via_algo(db=db, algo_id=algo_id)

def add_experiment(exp: TrainExperiment, db: Session = Depends(get_db)):
    return crud.db_create_exp(db=db,exp=exp)

def get_model( model_id: int,db: Session = Depends(get_db)):
    return crud.get_model(db=db, model_id=model_id)

def get_models(  exp_id:int,db: Session = Depends(get_db)):
    return crud.get_all_model_via_experiment(db=db, exp_id=exp_id)

def add_model(  model: Model,db: Session = Depends(get_db)):
    return crud.db_create_model(db=db, model=model)

def index():
    return "hello"