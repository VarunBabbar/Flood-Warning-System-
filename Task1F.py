from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
stations = build_station_list()
a = inconsistent_typical_range_stations(stations)
print(a)
