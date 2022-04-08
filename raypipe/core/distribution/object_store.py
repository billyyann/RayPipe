import os
import uuid
import base64
from abc import ABC
import sys

from raypipe import logger


def _strip_slash(path):
    contents=path.split("/")
    contents=[c for c in contents if len(c)]
    return "/".join(contents)

class ObjectPath:
    path:str
    object_name:str
    root:str="/tmp/object_store"
    prefix: str

    def create(self,path:str,object_name:str):
        self.path=_strip_slash(path)
        self.object_name=object_name
        self.prefix=str(uuid.uuid1())[:23]

    def get_path(self):
        return os.path.join(self.root,self.prefix,self.path,self.object_name)

    def get_encoded(self):
        return str(base64.b64encode(os.path.join(self.root,self.prefix,self.path,self.object_name))
        , encoding='utf-8')


class ObjectStore(ABC):
    def download(self, object_path: ObjectPath,target_path)->bytes:
        raise NotImplementedError("Please implement %s method" % sys._getframe().f_code.co_name)

    def upload(self, object_path: ObjectPath, file):
        raise NotImplementedError("Please implement %s method" % sys._getframe().f_code.co_name)

    def is_exist(self, object_path: ObjectPath):
        raise NotImplementedError("Please implement %s method" % sys._getframe().f_code.co_name)

    def clone(self, source_object_path: ObjectPath, target_object_path: ObjectPath):
        raise NotImplementedError("Please implement %s method" % sys._getframe().f_code.co_name)

    def state(self, object_path: ObjectPath):
        raise NotImplementedError("Please implement %s method" % sys._getframe().f_code.co_name)

    def delete(self, object_path: ObjectPath):
        raise NotImplementedError("Please implement %s method" % sys._getframe().f_code.co_name)


class FileSystemObjectStore(ObjectStore):
    """
    For single node deployment
    """
    def download(self, object_path: ObjectPath,target_path)->bytes:
        pass

    def upload(self, object_path: ObjectPath, file:bytes):
        #todo fix No such file or directory: '/tmp/object_store/95c3cae6-b4fc-11ec-bbfd/tmp/training'
        parent_path=os.path.dirname(object_path.get_path())
        if not os.path.exists(parent_path):
            os.makedirs( parent_path, exist_ok=True )
        with open(object_path.get_path()+".zip","wb") as f:
            f.write(file)

        logger.info("=========== checkpoint saved to %s =========== "%object_path.get_path())

    def is_exist(self, object_path: ObjectPath):
        pass

    def clone(self, source_object_path: ObjectPath, target_object_path: ObjectPath):
        pass

    def state(self, object_path: ObjectPath):
        pass

    def delete(self, object_path: ObjectPath):
        pass


class MemObjectStore(ObjectStore):
    pass


class S3ObjectStore(ObjectStore):
    def __init__(self):
        super.__init__()
    """
    For multi node deployment
    """
    pass

if __name__ == "__main__":
    # s = ObjectStore(**{"storage_type": "fs"})()
    # print(s.__class__)

    print(ObjectStore.__subclasses__())
