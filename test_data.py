from Task1C import run
from haversine import haversine
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
#Task 1C testing starts here
stations = build_station_list()
a = run()
for j in a:
    for i in stations:
        if i.name == j: # This statement ensures only the stations outputted in Task 1C are being tested for veracity
            reference_coordinate = (52.2053, 0.1218)
            b = i.coord
            assert haversine(b, reference_coordinate) <= 10 # Checks whether the station is actually 10 km from the city centre
#Task 1C testing ends here

g = stations_by_river(stations) #Task 1D testing starts here
q1 = g["River Aire"]
q2 = g['River Cam']
q3 = g['River Thames']
for j in q1:
    for i in stations:
        if i.river == j:
            assert i.river == "River Aire"
        elif i.river != j:
            assert i.river != "River Aire"


for j in q2:
    for i in stations:
        if i.river == j:
            assert i.river == "River Cam"
        elif i.river != j:
            assert i.river != "River Cam"
for j in q3:
    for i in stations:
        if i.river == j:
            assert i.river == 'River Thames'
        elif i.river != j:
            assert i.river != 'River Thames'
    #Task 1D testing ends here

