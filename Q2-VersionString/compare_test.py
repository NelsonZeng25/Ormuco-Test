import unittest
from version_compare import *

class TestCompare(unittest.TestCase):
    
    def test_numerical(self):
        version1 = "1.1.2"
        version2 = "1.1.1"
        self.assertEqual(compare(version1, version2), "1.1.2 is greater than 1.1.1")


if __name__ == '__main__':
    unittest.main()