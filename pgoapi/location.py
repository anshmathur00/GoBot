# Do NOT use this bot while signed into your acccount with your phone -TomTheBotter

import logging
from geopy.geocoders import GoogleV3
from gmaps.directions import *
import s2sphere
from geopy.distance import VincentyDistance, vincenty # Vincenty...
import pyproj
from time import time
g = pyproj.Geod(ellps='WGS84')
geolocator = GoogleV3()
def getLocation(search):
    loc = geolocator.geocode(search)
    return (loc.latitude, loc.longitude, loc.altitude)

def get_route(start,end, use_google = False, GMAPS_API_KEY = ""):
    origin = (start[0], start[1])
    destination = (end[0], end[1])
    if use_google:
        directions_service = Directions(api_key=GMAPS_API_KEY)
        d = directions_service.directions(origin, destination, mode="walking",units="metric")
        steps = d[0]['legs'][0]['steps']
        return [(step['end_location']["lat"],step['end_location']["lng"]) for step in steps]
    else:
        return [destination]

# step_size is how many meters we want; change that in config.json
def get_increments(start,end,step_size=200):
    g = pyproj.Geod(ellps='WGS84')
    (startlat, startlong, _) = start
    (endlat, endlong) = end
    (az12, az21, dist) = g.inv(startlong, startlat, endlong, endlat)
    # line paths that are <= 1 kilometer
    lonlats = g.npts(startlong, startlat, endlong, endlat,
                     1 + int(dist / step_size))
    lonlats.append((endlong, endlat))
    return [(l[1],l[0],0) for l in lonlats]




def distance_in_meters(p1,p2):
    return vincenty(p1,p2).meters

def filtered_forts(origin, forts):
    forts = [(fort, distance_in_meters(origin,(fort['latitude'], fort['longitude']))) for fort in forts if fort.get('type',None) == 1 and ("enabled" in fort or lure_info in fort) and fort.get('cooldown_complete_timestamp_ms',-1) < time()*1000]
    sorted_forts = sorted(forts, lambda x,y : cmp(x[1],y[1]))
    return [x[0] for x in sorted_forts]

def getNeighbors(loc, level=15, spread=700):
    distance = VincentyDistance(meters=spread)
    center = (loc[0], loc[1], 0)
    p1 = distance.destination(point=center, bearing=45)
    p2 = distance.destination(point=center, bearing=225)
    p1 = s2sphere.LatLng.from_degrees(p1[0], p1[1])
    p2 = s2sphere.LatLng.from_degrees(p2[0], p2[1])
    rect = s2sphere.LatLngRect.from_point_pair(p1, p2)
    region = s2sphere.RegionCoverer()
    region.min_level = level
    region.max_level = level
    cells = region.get_covering(rect)
    return sorted([c.id() for c in cells])
