import unittest
from versionCompare.version_compare import compare

class TestCompare(unittest.TestCase):
    def test_numerical(self):
        # ------- GREATER --------
        version1 = "1.1.2"
        version2 = "1.1.1"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        version1 = "1.5.1"
        version2 = "1.2.10"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        # ------- EQUAL --------
        version1 = "1.1.1"
        version2 = "1.1.1"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

        version1 = "550.221"
        version2 = "550.221"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

        # ------- LESSER --------
        version1 = "1.1.1"
        version2 = "1.1.2"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.1"
        version2 = "1.1.1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "2.0.1"
        version2 = "2.0.2"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)
    
    def test_pre_release(self):
        # ------- GREATER --------
        version1 = "1.1rc3"
        version2 = "1.1rc1"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        # ------- EQUAL --------
        version1 = "1.1a1"
        version2 = "1.1a1"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

        # ------- LESSER --------
        version1 = "1.2a3"
        version2 = "1.2rc3"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        version1 = "1.1a2"
        version2 = "1.1b2"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

    def test_dev(self):
        # ------- GREATER --------
        version1 = "1.1.dev50"
        version2 = "1.1.dev40"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        # ------- EQUAL --------
        version1 = "1.1.dev50"
        version2 = "1.1.dev50"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)
        
        # ------- LESSER --------
        version1 = "1.1.dev50"
        version2 = "1.1.dev555"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)
    def test_post(self):
        # ------- GREATER --------
        version1 = "1.1.3.post50"
        version2 = "1.1.3.post40"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        # ------- EQUAL --------
        version1 = "1.1.post50"
        version2 = "1.1.post50"
        self.assertEqual(compare(version1, version2), version1 + " is equal to " + version2)

        # ------- LESSER --------
        version1 = "1.1.post50"
        version2 = "1.1.post555"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

    def test_invalid_input(self):
        # ------- INVALID VERSION 1 --------

        # d not allowed
        version1 = "1.14d13"
        version2 = "1.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 1")

        # Too many "."
        version1 = "1.3.3.1.1.2"
        version2 = "1.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 1")

        # dev cannot be followed by a post
        version1 = "2.12.3.dev10.post12"
        version2 = "1.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 1")

        # No negative numbers
        version1 = "-3.1"
        version2 = "3.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 1")

        # ------- INVALID VERSION 2 --------
        
        # Cannot have version string without atleast 1 "."
        version1 = "2.3.dev22"
        version2 = "123"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 2")

        # Cannot have .dev after the first number
        version1 = "1.1.1"
        version2 = "2.dev22"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 2")

        # Cannot have .post after the first number
        version1 = "1.1.1"
        version2 = "2.post22"
        self.assertEqual(compare(version1, version2), "Invalid version format for version 2")

        # ------- INVALID BOTH VERSIONS --------
        
        # post has no number associated
        # v is not allowed
        version1 = "2.2a2.post"
        version2 = "v1.1"
        self.assertEqual(compare(version1, version2), "Invalid version format for both versions")

        # No "," allowed
        # Words are not allowed
        version1 = "3.3,2"
        version2 = "version 1"
        self.assertEqual(compare(version1, version2), "Invalid version format for both versions")

        # Pre release cannot have extra final release at the end
        # Pre release cannot be in micro
        version1 = "1.1a5.1"
        version2 = "1.1.4a4"
        self.assertEqual(compare(version1, version2), "Invalid version format for both versions")

        

    def test_mixed_inputs(self):
        # ------- GREATER --------

        # post > dev
        version1 = "2.45.post88"
        version2 = "2.45.dev88"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        # .dev > no .dev
        version1 = "1.5rc500.dev33"
        version2 = "1.5rc500"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        # Final release > Pre release
        version1 = "2.3.45"
        version2 = "2.3a5.dev45"
        self.assertEqual(compare(version1, version2), version1 + " is greater than " + version2)

        # ------- LESSER --------

        # Minor number > Minor number
        version1 = "1.2a23.dev35"
        version2 = "1.3a55.post44"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        # Major number > Major number
        version1 = "1.500000000.1"
        version2 = "2.1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        # Dev number > Dev number
        version1 = "5.1b45.post45.dev50"
        version2 = "5.1b45.post45.dev51"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        # dev < post
        version1 = "1.5.1.dev33"
        version2 = "1.5.1.post33"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        # Minor number > Minor number
        version1 = "2.4a45.post555.dev45"
        version2 = "2.5a45.post60.dev50"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        # Post number > Post number
        version1 = "1.34.post1.dev5000"
        version2 = "1.34.post2.dev1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        # .post < Final Release
        version1 = "1.2.post1"
        version2 = "1.2.1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)

        # .dev < Final Release
        version1 = "1.2.dev44"
        version2 = "1.2.1"
        self.assertEqual(compare(version1, version2), version1 + " is lesser than " + version2)


if __name__ == '__main__':
    unittest.main()