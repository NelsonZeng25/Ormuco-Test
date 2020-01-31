from cache import *
from math import sin, cos, sqrt, radians, atan2
from operator import itemgetter

# https://www.movable-type.co.uk/scripts/latlong.html
def distance(location1, location2):
    earthRadius = 6378000
    lat1 = radians(location1[0])
    lon1 = radians(location1[1])
    lat2 = radians(location2[0])
    lon2 = radians(location2[1])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return earthRadius * c


def createCaches(number, size, list, location):
    cacheDict = {}
    for i in range(number):
        cache = GeoDistLRUCache(5, (1,1))
        cacheDict[cache] = distance(location, cache.location)

    sortedCaches = sorted(cacheDict, key=itemgetter(1))
    return list(sortedCaches.keys())


if __name__ == '__main__':
    cacheList = []
    currentLocation = (0,0)


