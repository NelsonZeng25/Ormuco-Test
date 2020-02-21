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

    returns -> the distance between the 2 geolocations
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

def get(key, location, cacheList):
    """
    Used by the client to get a key from a cache
    Arguments:
    key         -> key that the client wants to retrieve from the cache
    location    -> (tuple) location of the client
    cacheList   -> (list) list of current available caches

    returns -> the value of the key from the closest cache
    """
    cacheDict = {}
    for cache in cacheList:
        cacheDict[cache] = distance(location, cache.location)
    sortedCaches = sorted(cacheDict, key=cacheDict.get)
    return sortedCaches[0].get(key)

