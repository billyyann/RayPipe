import os

from tensorflow.python.keras.callbacks import Callback, ModelCheckpoint
import ray.train as train
import zipfile

from raypipe import logger
from raypipe.core.distribution import object_store_impl
from raypipe.core.distribution.object_store import ObjectPath
from raypipe.core.rpipe.utils import zip_dir


class TrainReportCallback(Callback):
    def on_epoch_end(self, epoch:int, logs=None):
        train.report(**logs)


class DistModelSaveCallBack(ModelCheckpoint):
    def __init__(self,save_freq:int,verbose:int):
        self.FILE_PATH_template="/tmp/training/cp-{epoch:04d}.ckpt"
        super(DistModelSaveCallBack, self).__init__(
            filepath=self.FILE_PATH_template,
            save_freq=save_freq,
            verbose=verbose
        )

    @staticmethod
    def _upload(file_path):
        path_segments=file_path.split("/")
        object_path=ObjectPath()
        object_path.create("/".join(path_segments[:-1]),path_segments[-1])
        logger.info("=========== Object Path %s =========== "%object_path.get_path())

        zip_dir(file_path,file_path+".zip")

        with open(file_path+".zip","rb") as f:
            object_store_impl.upload(object_path,f.read())

    def on_train_batch_end(self, batch, logs=None):
        if self._should_save_on_batch(batch):
            self._save_model(epoch=self._current_epoch, logs=logs)
            file_path = self._get_file_path(self._current_epoch, logs)
            #todo distributed saving
            self._upload(file_path)
