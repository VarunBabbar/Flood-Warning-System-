# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
import numpy
from . import datafetcher
from .stationdata import build_station_list
from .station import MonitoringStation
from haversine import haversine
from .utils import sorted_by_key
import math

# formula for distance between two geographic coordinates (in km)
def haversine_formula(x1, y1, x2, y2):
    # difference in x and y
    d_X = (x2 - x1) * math.pi / 180.0
    d_Y = (y2 - y1) * math.pi / 180.0

    # converting x1 and x2 to radians
    x1 = x1 * math.pi / 180.0
    x2 = x2 * math.pi / 180.0

    a= math.sin(d_X/2)**2 + math.cos(x1)*math.cos(x2)*(math.sin(d_Y/2)**2)
    # radius,r of Earth (assuming that it is a perfect sphere)
    r = 6371
    distance = 2*r* math.asin(math.sqrt(a))
    return distance

#Task 1B
def stations_by_distance(stations, p):
    station_distance = []
    for station in stations:
        coord_p_distance = haversine_formula(station.coord[0], station.coord[1], p[0], p[1])
        name_distance = station.name, station.town, coord_p_distance
        station_distance.append(name_distance)
    sorted_stations = sorted_by_key(station_distance, 2, reverse=False)


    return sorted_stations

# Task 1C
def stations_within_radius(stations, centre, r):
    """Creates a list of stations within a given radius r of the reference coordinate """
    k = []
    for i in stations:
        distance = haversine(centre, i.coord)
        if distance <= r:
            k.append(i.name)
    return k

# Task 1D
def rivers_with_station(stations):
    """Creates a list of rivers with at least 1 station"""
    rivers = []
    for i in stations:
        if i.name != None:
            if i.river not in rivers:
                rivers.append(i.river)
    return rivers
def stations_by_river(stations):
    """Creates a dictionary of stations that are located on the same river. The river is the key for this dictionary"""
    river_dictionary = {}
    for i in stations:
        station_list = []
        for j in stations:
            if i.river == j.river:
                station_list.append(j.name)
        river_dictionary[i.river] = station_list
    return river_dictionary

#Task 1E
def rivers_by_station_number(stations, N):
    river_number_of_station=[]
    river_dictionary=stations_by_river(stations)
    for key in river_dictionary.keys():
        number_of_stations = len(river_dictionary[key])
        river_number = key, number_of_stations
        river_number_of_station.append(river_number)
    sorted_river_number = sorted_by_key(river_number_of_station, 1, reverse=True)

    n = 0
    if sorted_river_number[N][1] == sorted_river_number[N+1][1]:
        n = 0
        while sorted_river_number[N][1] == sorted_river_number[N+n+1][1]:
            n+=1
        return sorted_river_number[:N+n]
    elif sorted_river_number[N][1] != sorted_river_number[N+1][1]: 
        return sorted_river_number[:N]
