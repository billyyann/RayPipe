from tensorflow.python.keras.callbacks import Callback, ModelCheckpoint
import ray.train as train


class TrainReportCallback(Callback):
    def on_epoch_end(self, epoch:int, logs=None):
        train.report(**logs)


class DistModelSaveCallBack(ModelCheckpoint):
    def on_train_batch_end(self, batch, logs=None):
        if self._should_save_on_batch(batch):
            self._save_model(epoch=self._current_epoch, logs=logs)
            filepath = self._get_file_path(self._current_epoch, logs)
            #todo distributed saving