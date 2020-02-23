import unittest

def divide(a, b):
    print(a/b)

class NameTestCase(unittest.TestCase):
    def test_first(self):
        divide(1, 1)

    def test_second(self):
        divide(1, 2)

unittest.main()