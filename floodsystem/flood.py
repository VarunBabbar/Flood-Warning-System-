from .stationdata import update_water_levels
from .stationdata import build_station_list


def stations_level_over_threshold(stations ,tol):
    a = []
    b = []
    stations = build_station_list()
    update_water_levels(stations)
    for i in stations:
        if i.relative_water_level(i.latest_level) is not None:
            if i.relative_water_level(i.latest_level) > tol:
                b.append(i.relative_water_level(i.latest_level))
    b.sort(reverse = True)
    for j in b:
        for k in stations:
            if j == k.relative_water_level(k.latest_level):
                a.append((k.name, j))
    return a
