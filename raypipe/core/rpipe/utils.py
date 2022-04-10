import os
import zipfile

import ray
from ray.train import Trainer

from raypipe.core.data_model import RayConfig, TrainerConfig


def start_ray(ray_config:RayConfig):
    try:
        ray.init(address=ray_config.address,
                 _redis_password=ray_config.redis_password,
                 runtime_env=ray_config.runtime_env
                 )
    except:
        ray.init()

def build_ray_trainer(trainer_config:TrainerConfig):
    return  Trainer(backend=trainer_config.backend,
                    num_workers=trainer_config.num_workers,
                    use_gpu=trainer_config.use_gpu)


def zip_dir(dirpath, zip_name):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param zip_name: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()