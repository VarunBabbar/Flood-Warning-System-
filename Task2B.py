from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()
update_water_levels(stations)
tol = 0.8
print("Stations with a relative water level greater than tolerance:")
print(stations_level_over_threshold(stations, tol))
