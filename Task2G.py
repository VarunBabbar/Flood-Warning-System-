from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels2

from datetime import datetime, timedelta, date, time
import datetime

import io
import pygame as pg
import time
import request
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen


def risk_criterion_analyser(tol, days):
    stations = build_station_list()
    update_water_levels(stations)
    a = stations_level_over_threshold(stations, tol)
    m = []
    for i in a:
        m.append(i[0])

    for i in stations:
        for name in m:
            if name == i.name:
                lol = []
                for k in fetch_measure_levels(i.measure_id, dt = timedelta(days = days))[1]:
                    p = (float(k) - float(i.typical_range[0])) / (float(i.typical_range[1]) - float(i.typical_range[0]))
                    lol.append(p)
                plot_water_levels2(i, fetch_measure_levels(i.measure_id, dt = timedelta(days = days))[0], lol)
    mean_list = []

    for i in stations:
        for name in m:
            if name == i.name:
                lol2 = []
                L = 0
                lol3 = []
                L2 = 0
                for k in fetch_measure_levels(i.measure_id, dt = timedelta(days = 10000))[1]:
                    p = (float(k) - float(i.typical_range[0])) / (float(i.typical_range[1]) - float(i.typical_range[0]))
                    lol2.append(p)
                    if p > 1.2: #1.2 times relative typical high
                        L += 1
                        lol3.append(p)
                        summation = 0
                        for member in lol3:
                            summation += member
                if L != 0:
                    mean = summation / L # Mean of all relative water level values which are greater than 1.2
                    mean_list.append(mean)
                lol4 = []
                L3 = 0
                lol5 = []
                L4 = 0
                for k2 in fetch_measure_levels(i.measure_id, dt = timedelta(days = days))[1]:
                    p2 = (float(k2) - float(i.typical_range[0])) / (float(i.typical_range[1]) - float(i.typical_range[0]))
                    lol4.append(p2)
                    if p2 > 1.5 * mean: # Caution if water level is greater than 1.5 times mean for an extended cumulative period of time
                        L3 += 1
                print(L3)
                if L3 > 25*days:
                    print("Severe Risk of Flooding for Station {}".format(i.name))
                elif 25*days >= L3 > 10*days:
                    print("High Risk of Flooding for Station {}".format(i.name))
                elif 10*days >=  L3 > 5*days:
                    print("Moderate Risk of Flooding for Station {}".format(i.name))
                elif L3 <= 5*days:
                    print("Low Risk of Flooding for Station {}".format(i.name))

    print(mean_list)


    #
    #
    # pg.init()
    #
    # image_url = "https://athensema.files.wordpress.com/2013/07/flood-warning.jpg"
    # image_str = urlopen(image_url).read()
    # image_file = io.BytesIO(image_str)
    # white = (255, 255, 255)
    # # create a 600x400 white screen
    # screen = pg.display.set_mode((1600, 1400), pg.RESIZABLE)
    # screen.fill(white)
    # # load the image from a file or stream
    # image = pg.image.load(image_file)
    # screen.bilt(image, (0, 0))
    # pg.display.flip()
    #
    # while True:
    #     for event in pg.event.get():
    #         if event.type == pg.QUIT:
    #             pg.quit()
    #             raise SystemExit

    return

print(risk_criterion_analyser(1.2, 10))




    # Need relative levels for N days behind. U have absolute levels available



# Basically, assign a risk value depending on the following factors:
# Historically, how has the data varied. Consider the all time high, look up if the station has experienced flooding at that all time high,
# and if it is within 20% of this value, then risk = severe
# Also consider the relative water level: if it is over 0.9 then high, over 0.8 then moderate, over 0.7 then low
# Consider the rate of uptake of water: Warning if the rate of increase of relative water level is greater than a threshold value
# Consider if you can play a sound and output a warning image using pygame (lol) if the risk is severe:
# Show all stations on a map
# https://athensema.files.wordpress.com/2013/07/flood-warning.jpg
