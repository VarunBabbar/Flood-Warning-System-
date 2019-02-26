

from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

stations = build_station_list()
print("N stations with the highest relative water level:")
print(stations_highest_rel_level(stations, 10))