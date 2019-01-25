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
