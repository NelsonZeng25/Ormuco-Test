import unittest
from version_compare import compare

class TestCompare(unittest.TestCase):
    def test_numerical(self):
        version1 = "1.1.2"
        version2 = "1.1.1"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "1.1.1"
        version2 = "1.1.1"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

        version1 = "1.1.1"
        version2 = "1.1.2"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.1"
        version2 = "1.1.1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.5.1"
        version2 = "1.2.10"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "2.0.1"
        version2 = "2.0.2"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)
    
    def test_pre_release(self):
        version1 = "1.1a2"
        version2 = "1.1b2"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.1rc3"
        version2 = "1.1rc1"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "1.1a1"
        version2 = "1.1a1"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

        version1 = "1.2a3"
        version2 = "1.2rc3"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

    def test_dev(self):
        version1 = "1.1.dev50"
        version2 = "1.1.dev555"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.1.dev50"
        version2 = "1.1.dev40"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "1.1.dev50"
        version2 = "1.1.dev50"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

    def test_post(self):
        version1 = "1.1.post50"
        version2 = "1.1.post555"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.1.3.post50"
        version2 = "1.1.3.post40"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "1.1.post50"
        version2 = "1.1.post50"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

    def test_invalid_input(self):
        version1 = "1.14d13"
        version2 = "1.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 1")

        version1 = "1.3.3.1.1.2"
        version2 = "1.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 1")

        version1 = "2.12.3.dev10.post12"
        version2 = "1.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 1")

        version1 = "2.2a2.post"
        version2 = "1.1.v.3"
        self.assertEqual(compare(version1, version2), "Invalid version format for both versions")

        version1 = "2.3.dev22"
        version2 = "123"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 2")

        version1 = "3.3,2"
        version2 = "version 1"
        self.assertEqual(compare(version1, version2), "Invalid version format for both versions")

    def test_mixed_inputs(self):
        version1 = "1.2a23.dev35"
        version2 = "1.3a55.post44"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "2.3.45"
        version2 = "2.3a5.dev45"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "1.500000000.1"
        version2 = "2.1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.5rc500.dev33"
        version2 = "1.5rc500"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "5.1b45.post45.dev50"
        version2 = "5.1b45.post45.dev51"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.5.1.dev33"
        version2 = "1.5.1.post33"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "2.4a45.post555.dev45"
        version2 = "2.5a45.post60.dev50"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.34.post1.dev5000"
        version2 = "1.34.post2.dev1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "2.45.post88"
        version2 = "2.45.dev88"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)




if __name__ == '__main__':
    unittest.main()