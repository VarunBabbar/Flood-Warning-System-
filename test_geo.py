

from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from haversine import haversine

# Build list of stations
stations = build_station_list()

#Task 1B

def test_stations_by_distance():
    result = stations_by_distance(stations, p=(0,0))
    for i in range(1, len(result)):
        x = result[i]
        y = result[i-1]
        assert x[2] >= y[2]

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



             



