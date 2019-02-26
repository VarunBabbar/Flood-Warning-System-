import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date, time
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold


stations = build_station_list()
a = stations_level_over_threshold(stations, 0.8)
x = a[:5]
m = []
for i in range(0,5):
    m.append(x[i][0])
print(m)

for i in stations:
    for k in m:
        if k == i.name:
            dates, levels = fetch_measure_levels(i.measure_id, dt = timedelta(days = 2))
            plot_water_level_with_fit(i, dates, levels, 4)