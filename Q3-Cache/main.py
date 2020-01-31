from cache import *
from math import sin, cos, sqrt, radians, atan2
from operator import itemgetter
import csv
from random import randint

# https://www.movable-type.co.uk/scripts/latlong.html
def distance(location1, location2):
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


def createCaches(number, size, location):
    cacheDict = {}
    with open('Q3-Cache/capitals.csv','rt') as file:
        reader = csv.reader(file)
        rows = [r for r in reader]

    for i in range(number):
        rowIndex = randint(1,len(rows))
        cacheLocation = (float(rows[rowIndex][2]), float(rows[rowIndex][3]))

        cache = GeoDistLRUCache(size, cacheLocation)
        cacheDict[cache] = distance(location, cache.location)

    sortedCaches = sorted(cacheDict, key=cacheDict.get)
    return sortedCaches


if __name__ == '__main__':
    currentLocation = (45.508888, -73.561668)       # Montreal Longitude and Latitude
    cacheList = createCaches(5, 5, currentLocation)

    for i in cacheList:
        print(i.location, distance(currentLocation, i.location))

