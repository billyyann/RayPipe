import unittest

from raypipe.core.algos.cnn import CNN

class CNNTester(unittest.TestCase):
    def test_cnn_remote_train(self):
        general_cfg={
            "algorithm_cfg":{
                "name":CNN
            },
            "ray_cfg":{
                "address":'127.0.0.1:6379',
                # "address":"ray://172.27.69.28:32071",
                "redis_password" : '5241590000000000',
                "runtime_env":{}
            },
            "trainer_cfg":{
                "backend":"tensorflow",
                "type":"keras",
                "num_workers":1,
                "use_gpu":False
            },
            "learning_cfg":{
                "lr":1e-3,
                "batch_size": 10,
                "epochs": 15,
                "steps_per_epoch": 3
            }
        }
        cnn=CNN(**general_cfg)
        cnn.train(method="remote")

