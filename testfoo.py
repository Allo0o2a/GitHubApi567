import unittest
from unittest import mock
import foo

class FooTest(unittest.TestCase):
    def test_foo(self):
        x = foo.foo(3)
        print("not mocked", x)

    @mock.patch('foo.foo')
    def test_foo2(self, mk):
        mk.return_value = 99
        print("calling mocked foo")
        x = foo.foo(3)
        print("mocked foo={}".format(x))


if __name__ == "__main__":
    unittest.main()