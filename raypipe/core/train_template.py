import tensorflow as tf
import os

from raypipe.core.rpipe.callback import DistModelSaveCallBack
from raypipe import logger

def keras_train_template(general_config):
    learning_config = general_config.get("learning_config")
    trainer_config = general_config.get("trainer_config")
    data_cfg = general_config.get("data_cfg")
    model_strategy_func=general_config.get("model_strategy_func")
    data_generator_func=general_config.get("data_generator_func")

    strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy()
    logger.info('=========== strategy initialized =========== ')

    with strategy.scope():
        multi_worker_model = model_strategy_func(learning_config.dict())

    logger.info('=========== Model built =========== ')

    global_batch_size = learning_config.batch_size * trainer_config.num_workers
    batch_dataset = data_generator_func(data_cfg, global_batch_size)

    logger.info('=========== Dataset downloaded =========== ')

    if not os.path.exists("/tmp/training"):
        os.mkdir("/tmp/training")

    epoch_call_back = DistModelSaveCallBack(save_freq=learning_config.batch_size,
                                            verbose=1)
    history = multi_worker_model.fit(
        batch_dataset,
        epochs=learning_config.epochs,
        steps_per_epoch=learning_config.steps_per_epoch,
        callbacks=[epoch_call_back])

    results = history.history
    return results