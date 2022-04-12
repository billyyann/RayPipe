from sqlalchemy.orm import Session
from . import models, schemas


def get_algorithm(db: Session, algo_id: int):
    return db.query(models.Algorithm).filter(models.Algorithm.id == algo_id).first()

def db_create_user(db: Session, algo: schemas.Algorithm):
    db_algo = models.Algorithm(
        model_name =algo.model_name,
    )
    db.add(db_algo)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_algo)  # 刷新
    return db_algo

def get_algorithm(db: Session):
    return db.query(models.Algorithm).all()

def db_create_algo(db: Session, algo: schemas.Algorithm):
    db_algo = models.Algorithm(
        algorithm_name =algo.algorithm_name,
    )
    db.add(db_algo)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_algo)  # 刷新
    return db_algo

def get_experiment(db: Session, exp_id: int):
    return db.query(models.TrainExperiment).filter(models.TrainExperiment.id == exp_id).first()

def get_all_experiments_via_algo(db: Session, algo_id:int):
    return db.query(models.TrainExperiment).filter(models.TrainExperiment.algorithm_id == algo_id)

def db_create_exp(db: Session, exp: schemas.TrainExperiment):
    db_exp = models.TrainExperiment(
        algorithm_name=exp.algorithm_name,
        train_params=exp.train_params
    )
    db.add(db_exp)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_exp)  # 刷新
    return db_exp

def get_model(db: Session, model_id: int):
    return db.query(models.Model).filter(models.Model.id == model_id).first()

def get_all_model_via_experiment(db:Session, exp_id:int):
    return db.query(models.Model).filter(models.Model.exp_id == exp_id).first()

def db_create_model(db: Session, model: schemas.Model):
    db_model = models.Model(
        exp_id=model.exp_id,
        save_path =model.save_path
    )
    db.add(db_model)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_model)  # 刷新
    return db_model
