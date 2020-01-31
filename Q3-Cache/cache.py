from collections import deque
import time

class GeoDistLRUCache(object):
    
    def __init__(self, size, location, values = {}, initialTimes = {}, expirationTimes = {}, priorityQueue = deque()):
        self.size = size
        self.location = location
        self.values = values
        self.initialTimes = initialTimes
        self.expirationTimes = expirationTimes
        self.priorityQueue = priorityQueue

    def get(self, key):
        self.checkExpiration()
        if (key not in self.priorityQueue):
            print("Cache Miss!")
            # This is where you add the Query method to access the database
            return ValueError()

        self.priorityQueue.remove(key)
        self.priorityQueue.appendleft(key)
        return self.values[key]

    def put(self, key, value, expirationTime = 100):
        self.checkExpiration()
        if (key in self.priorityQueue):
            return "Key is already in cache"
        elif (len(self.priorityQueue) == self.size):
            lastKey = self.priorityQueue.pop()
            self.values.pop(lastKey)
        
        self.priorityQueue.append(key)
        self.values[key] = value
        self.initialTimes[key] = time.time()
        self.expirationTimes[key] = expirationTime
        
    def checkExpiration(self):
        for key, initialTime in self.initialTimes.items():
            if (time.time() > initialTime + self.expirationTimes[key]):
                self.priorityQueue.remove(key)
                self.values.pop(key)
                self.initialTimes.pop(key)
                self.expirationTimes.pop(key)
        return