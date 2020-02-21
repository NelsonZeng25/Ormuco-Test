from cache import GeoDistLRUCache
from math import sin, cos, sqrt, radians, atan2
from operator import itemgetter
import csv
from random import randint

# https://www.movable-type.co.uk/scripts/latlong.html
def distance(location1, location2):
    """ Finds the distance between 2 geolocations
    Arguments:
    location1 -> (tuple) Geolocation of the first location (latitude, longitude)
    location2 -> (tuple) Geolocation of the second location (latitude, longitude)
    """
    earthRadius = 6378.0
    lat1 = radians(location1[0])
    lon1 = radians(location1[1])
    lat2 = radians(location2[0])
    lon2 = radians(location2[1])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return earthRadius * c


def createRandomCaches(size, location, number):
    """ Creates a number of caches at random locations using capitals.csv
    Arguments:
    size        -> (int) The size of each cache
    location    -> (tuple) location of the user
    number      -> (int) The number of created caches
    """
    cacheDict = {}
    with open('Q3-Cache/capitals.csv','rt') as file:
        reader = csv.reader(file)
        rows = [r for r in reader]

    for i in range(number):
        rowIndex = randint(1,len(rows))
        cacheLocation = (float(rows[rowIndex][2]), float(rows[rowIndex][3]))

        cache = GeoDistLRUCache(size, cacheLocation)
        cacheDict[cache] = distance(location, cache.location)

    return sorted(cacheDict, key=cacheDict.get)

def createSpecificCaches(size, location, locationList):
    """ Creates a number of caches at random locations using capitals.csv
    Arguments:
    size         -> (int) The size of each cache
    location     -> (tuple) location of the user
    locationList -> (list) List of of tuples containing the locations where we want to create our caches
    """
    cacheDict = {}
    for l in locationList:
        cache = GeoDistLRUCache(size, l)
        cacheDict[cache] = distance(location, cache.location)
    return sorted(cacheDict, key=cacheDict.get)

def get(key, location, cacheList):
    cacheDict = {}
    for cache in cacheList:
        cacheDict[cache] = distance(location, cache.location)
    sortedCaches = sorted(cacheDict, key=cacheDict.get)
    return sortedCaches[0].get(key)

