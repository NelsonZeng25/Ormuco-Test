import unittest
from helper import createSpecificCaches
from cache import GeoDistLRUCache

class TestCache(unittest.TestCase):
    
    currentLocation = (45.508888, -73.561668)

    def test_GetValue(self):
        cache = GeoDistLRUCache(5, (38.907192,-77.036871))
        cache.put(1, "hello")
        self.assertEqual("hello", cache.get(1))

        cache.put(2, 4444)
        self.assertEqual(4444, cache.get(2))
    
    def test_GetValue_Error(self):
        cache = GeoDistLRUCache(1, (38.907192,-77.036871))
        self.assertRaises(ValueError, cache.get, 1)

        cache.put(1, "hello")
        cache.put(2, "world")
        self.assertRaises(ValueError, cache.get, 1)

    def test_PutValue(self):
        cache = GeoDistLRUCache(5, (38.907192,-77.036871))
        cache.put(1, "hello")
        self.assertEqual({1 : "hello"}, cache.values)

        cache.put(2, "world")
        self.assertEqual({1: "hello", 2: "world"}, cache.values)

    def test_GetClosestCache(self):
                    # United States             Germany              Canada
        caches = [(38.907192,-77.036871), (52.520007,13.404954),(45.42153,-75.697193)]

                    #   Canada                    United States             Germany
        sortedCache = [(45.42153,-75.697193), (38.907192,-77.036871), (52.520007,13.404954)]

        cacheList = createSpecificCaches(3, self.currentLocation, caches)
        temp = []
        for cache in cacheList:
            temp.append(cache.location)

        self.assertEqual(temp, sortedCache)
    


if __name__ == '__main__':
    unittest.main()