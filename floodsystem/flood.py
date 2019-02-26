from .stationdata import update_water_levels
from .stationdata import build_station_list
from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations ,tol):
    a = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level(station.latest_level) is not None:
            if station.relative_water_level(station.latest_level) > tol:
                station_name_water_level = station.name, station.relative_water_level(station.latest_level)
                a.append(station_name_water_level)
    b = sorted_by_key(a, 1, reverse=True)
    return b


def stations_highest_rel_level(stations, N):
    a = []
    update_water_levels(stations)
    for station in stations:
        if station.relative_water_level(station.latest_level) is not None:
            station_name_water_level = station.name, station.relative_water_level(station.latest_level)
            a.append(station_name_water_level)
    b = sorted_by_key(a, 1, reverse=True)
    return b[:N]

       
