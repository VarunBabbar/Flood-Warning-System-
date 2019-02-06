from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
stations = build_station_list()
r = rivers_with_station(stations)
r.sort()
print(len(r))
print(r[:10])
g = stations_by_river(stations)
q1 = g["River Aire"]
q2 = g['River Cam']
q3 = g['River Thames']
print("Stations on River Aire: {}".format(q1))
print("Stations on River Cam: {}".format(q2))
print("Stations on Thames: {}".format(q3))
