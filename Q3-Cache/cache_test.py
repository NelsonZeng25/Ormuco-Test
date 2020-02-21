import unittest
import time
import helper
from cache import GeoDistLRUCache

class TestCache(unittest.TestCase):
    
    # Montreal         Latitude and Longitude
    currentLocation = (45.508888, -73.561668)

    def test_Get_Value(self):
        cache = GeoDistLRUCache(5, (38.907192,-77.036871))
        cache.put(1, "hello")
        self.assertEqual("hello", cache.get(1))

        cache.put(2, 4444)
        self.assertEqual(4444, cache.get(2))
    
    def test_Get_Value_Error(self):
        cache = GeoDistLRUCache(1, (38.907192,-77.036871))
        self.assertRaises(ValueError, cache.get, 1)

        cache.put(1, "hello")
        cache.put(2, "world")
        self.assertRaises(ValueError, cache.get, 1)

    def test_Put_Value(self):
        cache = GeoDistLRUCache(5, (38.907192,-77.036871))
        cache.put(1, "hello")
        self.assertEqual({1 : "hello"}, cache.values)

        cache.put(2, "world")
        self.assertEqual({1: "hello", 2: "world"}, cache.values)

    def test_Put_Value_Error(self):
        cache = GeoDistLRUCache(1, (38.907192,-77.036871))
        cache.put(1, "hello")
        self.assertEqual("Key is already in cache", cache.put(1, "hello"))

    def test_Overwrite_Value(self):
        cache = GeoDistLRUCache(1, (38.907192,-77.036871))
        cache.put(1, "hello")
        cache.put(1, "world")
        self.assertEqual("world", cache.get(1))

    def test_Popping_LRU_Items(self):
        cache = GeoDistLRUCache(4, (38.907192,-77.036871))
        cache.put(1, "hello")
        cache.put(2, "world")
        cache.put(3, "good")
        cache.put(4, "day")

        cache.get(2)    # Least recently used
        cache.get(4)    # 2nd Least recently used
        cache.get(1)
        cache.get(3)

        cache.put(5, "to you")  # Replaces key = 2

        self.assertEqual({1: "hello", 3: "good", 4: "day", 5: "to you"}, cache.values)

        cache.put(6, "Okay")    # Replaces key = 4

        self.assertEqual({1: "hello", 3: "good", 5: "to you", 6: "Okay"}, cache.values)

    def test_Expiration(self):
        cache = GeoDistLRUCache(1, (38.907192,-77.036871))
        cache.put(1, "hello", 1)
        self.assertEqual({1: "hello"}, cache.values)
        time.sleep(1)
        self.assertRaises(ValueError, cache.get, 1)

    def test_Get_Closest_Cache(self):
                # United States (2nd closest)   Germany (furthest)    Canada (closest)
        locations = [(38.907192,-77.036871), (52.520007,13.404954),(45.42153,-75.697193)]

        cache1 = GeoDistLRUCache(1, locations[0])
        cache1.put(1, "USA")
        cache2 = GeoDistLRUCache(1, locations[1])
        cache2.put(1, "Germany")
        cache3 = GeoDistLRUCache(1, locations[2])
        cache3.put(1, "Canada")

        cacheList = [cache1, cache2, cache3]
        
        self.assertEqual("Canada", helper.get(1, self.currentLocation, cacheList))

if __name__ == '__main__':
    unittest.main()