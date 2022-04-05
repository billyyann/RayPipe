import io
import unittest
import uuid

from raypipe.core.distribution.object_store import ObjectPath, _strip_slash


class UtilsTest(unittest.TestCase):
    def test_uuid(self):
        print((str(uuid.uuid1())[:23]))

    def test_ObjectPath(self):
        o=ObjectPath()
        o.create("xxx","1.txt")
        print(o.get_path())

    def test_strip_slash(self):
        print(_strip_slash("/tmp/1/2/3/"))

    def test_bytes(self):
        f=io.BytesIO(b"some initial binary data: \x00\x01")
        print(type(f.read()))

    def test_object2bytes(self):
        a=[1,23,3,4]
        b=bytes(a)
        c = io.BytesIO(b)
        # view[2:4] = b"56"
        print(c.read().decode())
