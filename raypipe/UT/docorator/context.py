import unittest

from raypipe.core.distribution import ObjectStore


class ContextTester(unittest.TestCase):
    def test_autowire(self):
        print(ObjectStore)
