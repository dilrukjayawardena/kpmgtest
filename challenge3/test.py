import nested as nt
import json
import unittest

class TestStringMethods(unittest.TestCase):
    def test_dt1(self):
        data={"a":{"b":{"c":"d"}}}
        key='a/b/c'
        self.assertEqual(nt.get_key(data,key), 'd')
    
    def test_dt2(self):
        data={"x":{"y":{"z":"a"}}}
        key='x/y/z'
        self.assertEqual(nt.get_key(data,key), 'a')


if __name__ == '__main__':
    unittest.main()