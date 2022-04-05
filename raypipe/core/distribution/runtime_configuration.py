import os

from raypipe.core import rpipe
from raypipe.core.distribution.object_store import ObjectStore


@rpipe.bean(class_name=os.environ.get('object_store',"FileSystemObjectStore"))
def object_store(kclass=ObjectStore):
    return kclass



