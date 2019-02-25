from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels


stations = build_station_list()
def test_stations_level_over_threshold():
    tol = 0.8
    update_water_levels(stations)
    a = stations_level_over_threshold(stations, tol)
    for i in stations:
        for j in a:
            if j[0] == i.name:
                assert j[1] == i.relative_water_level(i.latest_level)
                assert j[1] > 0.8

    return
