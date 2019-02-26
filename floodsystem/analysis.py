
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta, date, time
from .datafetcher import fetch_measure_levels
from .stationdata import build_station_list

def polyfit(dates, levels, p):
    dates_float = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(dates_float-dates_float[0], levels, p)
    poly = np.poly1d(p_coeff)
    a=[]
    b=dates_float
    c = []
    for item in b:
        lol = item - dates_float[0]
        c.append(lol)
    for date in dates_float:
        dates_shifted = date -dates_float[0]
        a.append(poly(dates_shifted))

    return a, c

        