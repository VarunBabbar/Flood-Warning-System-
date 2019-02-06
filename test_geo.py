
from floodsystem.geo import stations_by_distance, rivers_by_station_number
from haversine import haversine
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations

# Build list of stations
stations = build_station_list()

#Task 1B

def test_stations_by_distance():
    result = stations_by_distance(stations, p=(0,0))
    for i in range(1, len(result)):
        x = result[i]
        y = result[i-1]
        assert x[2] >= y[2]

# Testing Task C: Are all the outputted stations within 10 km of the city centre
def test_stations_within_radius():
    stations = build_station_list()
    reference_coordinate = (52.2053, 0.1218)
    lol = stations_within_radius(stations,reference_coordinate,10)
    for i in stations:
        for a in lol:
            if i.name == a:
                assert haversine(reference_coordinate, i.coord) <= 10

#Testing Task D: Do all rivers outputted have at least 1 station?
def test_rivers_with_station():
    stations = build_station_list()
    r = rivers_with_station(stations)
    assert len(r) == 857
    for i in stations:
        for j in r:
            a = 0
            if i.river == j:
                a = a+1
                assert a>= 1
#Testing Task D: Are all the stations outputted situated on the desired rivers?
def test_stations_by_river():
    stations = build_station_list()
    r1 = stations_by_river(stations)
    g1 = r1["River Aire"]
    g2 = r1['River Cam']
    g3 = r1['River Thames']
    for i in stations:
        for j in g1:
            if i.name == g1:
                assert i.river == "River Aire"
        for k in g2:
            if i.name == g2:
                assert i.river == "River Cam"
        for l in g3:
            if i.name == g3:
                assert i.river == "River Thames"

#Task 1E
def test_rivers_by_station_number():
    N = 9
    result = rivers_by_station_number(stations, N)
    assert len(result) >= 9

    if len(result) == N:
        for n in range(len(result)-1):
            x = result[n]
            y = result[n+1]
            assert x[1] >= y[1]
    elif len(result) > N:
        for n in range(N-1):
            x = result[n]
            y = result[n+1]
            assert x[1] >= y[1]
        for n in range(N, len(result)-1):
            x = result[n]
            y = result[n+1]
            assert x==y


# Testing Task F: Do all outputted stations have inconsistent range data
def test_inconsistent_typical_range_stations():
    stations = build_station_list()
    r2 = inconsistent_typical_range_stations(stations)
    for i in stations:
        for j in r2:
            if i.name == j:
                assert i.typical_range == None or i.typical_range[1] - i.typical_range[0] < 0





             



