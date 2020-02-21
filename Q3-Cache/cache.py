from collections import deque
import time

class GeoDistLRUCache:
    
    def __init__(self, size, location):
        """ Initialize Cache
        For every dictionary, they all have common keys
        Arguments:
        size            -> (int) how many items the cache can hold
        location        -> (tuple) geolocation of the cache (latitude, longitude)
        values          -> (dict) value of the items with a key associated to it
        intialTimes     -> (dict) the time that it was added to the cache with the associated key
        expirationTimes -> (dict) how long the item can last in the cache before being expired. Also with the associated key
        priorityQueue   -> (deque()) Queue used to sort the items from LRU to MRU.
        """
        self.size = size
        self.location = location
        self.values = {}
        self.initialTimes = {}
        self.expirationTimes = {}
        self.priorityQueue = deque()

    def get(self, key):
        """ 
        First, check the cache for expiration and get rid of all expired items
        Second, it checks if there's a cache miss.
            If yes, this is where you will add the Query method access the item from the database
            If not, it puts the item to MRU and returns the value of the key
        """
        self.checkExpiration()
        if (key not in self.priorityQueue):
            raise ValueError("Key not found in cache")

        self.priorityQueue.remove(key)
        self.priorityQueue.appendleft(key)
        return self.values[key]

    def put(self, key, value, expirationTime = 100):
        """
        First, check the cache for expiration and get rid of all expired items
        Second, check for valid inputs
        Third, if key is already in the Cache, 
            If the value is also the same, update the initial time and return error message
            If the value is not the same, overwrite the previous key with new value
        Fourth, if the cache is full, it gets rid of the LRU item

        Then, it adds the item to the MRU spot of the Cache with its value, time and expiration time.
        """
        self.checkExpiration()
        
        if (key == None or value == None or expirationTime == None):
            raise TypeError("Invalid input")
        if (expirationTime <= 0):
            raise ValueError("Invalid experation time")

        if (key in self.priorityQueue):
            if (value == self.values[key]):
                self.initialTimes[key] = time.time()
                return "Key is already in cache"
            else:
                self.priorityQueue.remove(key)

        elif (len(self.priorityQueue) == self.size):
            lastKey = self.priorityQueue.pop()
            self.values.pop(lastKey)
            self.initialTimes.pop(lastKey)
            self.expirationTimes.pop(lastKey)
        
        self.priorityQueue.appendleft(key)
        self.values[key] = value
        self.initialTimes[key] = time.time()
        self.expirationTimes[key] = expirationTime
        
    def checkExpiration(self):
        """
        Goes through all the keys in the cache and gets rid of all expired items
        """
        for key in list(self.initialTimes):
            if (time.time() > self.initialTimes[key] + self.expirationTimes[key]):
                self.priorityQueue.remove(key)
                self.values.pop(key)
                self.initialTimes.pop(key)
                self.expirationTimes.pop(key)