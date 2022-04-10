
from raypipe import logger
from raypipe.core import rpipe


from raypipe.core.data_model import LearningConfig

from raypipe.core.rpipe.utils import build_ray_trainer
from raypipe.core.train_template import keras_train_template


@rpipe.init
class ModelProxy:
    def __init__(self, model_strategy_func,data_generator_func):
        """
        paras as model config
        :param kwargs:
        """
        self._validate_model(model_strategy_func)
        self._validate_learning_config(self._learning_config)

        self.model_strategy_func = model_strategy_func
        self.data_generator_func=data_generator_func
        self._train_template=self.select_train_template(self._trainer_config.type)
        self.ray_trainer = build_ray_trainer(self._trainer_config)

        if not self.ray_trainer: raise NotImplementedError("Trainer not built.")
        self.initialized=True

    @staticmethod
    def select_train_template(t_type:str):
        """
        to extend trainer template here
        eg. keras, pytorch, tf1, tf2, simulation, optimization
        :param t_type:
        :return:
        """
        if t_type=="keras":
            return keras_train_template

    @rpipe.is_init
    def _validate_env(self):
        if not self.initialized:
            raise EnvironmentError("Model distribution not initialized")

    def _validate_model(self,model):
        #todo
        pass

    def _validate_learning_config(self, config:LearningConfig):
        #todo
        pass

    def local_train(self,dataset):
        self._validate_env()
        local_model=self.model_strategy_func(self.learning_cfg)
        local_model.fit(dataset)

    def local_eval(self):
        pass

    def submit(self):
        """
        :return:
        """
        self._validate_env()
        self.ray_trainer.start()
        logger.info('=========== Trainer started =========== ')


        self.ray_trainer.run(
            train_func=self._train_template,
            config={
                    "learning_config":self._learning_config,
                    "trainer_config":self._trainer_config,
                    "data_cfg":self._data_cfg,
                    "model_strategy_func": self.model_strategy_func ,
                    "data_generator_func": self.data_generator_func
                    }
            )

    def upload(self):
        """
        :return:
        """
        self._validate_env()


    def collect(self):
        """
        :return:
        """
        self._validate_env()

    def shutdown(self):
        self.ray_trainer.shutdown()
        self.ray_trainer=None
        logger.info('=========== Model training ended =========== ')



