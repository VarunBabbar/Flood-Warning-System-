import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta, date, time
from .datafetcher import fetch_measure_levels
from .stationdata import build_station_list


def plot_water_levels(station, dates, levels):
    plt.plot(dates, levels)
    plt.xlabel("Date")
    plt.ylabel("Water Level (m)")

    plt.xticks(rotation = 45);
    plt.title("Station {}".format(station.name))

    plt.tight_layout()
    plt.show()
    return
