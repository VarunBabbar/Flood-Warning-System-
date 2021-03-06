# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        return d

# Task 1F
    def typical_range_consistent(self):
        return self.typical_range is not None and float(self.typical_range[1]) - float(self.typical_range[0]) >= 0

<<<<<<< HEAD
# Task 2B
    def relative_water_level(self, latest_level):
       if latest_level is not None and self.typical_range_consistent():
           return (float(latest_level) - float(self.typical_range[0]))/(float(self.typical_range[1]) - float(self.typical_range[0]))
       else: 
           return None

# Task 1F
=======
# Task 2B:
    def relative_water_level(self, latest_level):
            x = self.typical_range is not None and float(self.typical_range[1] - self.typical_range[0]) >= 0
            if x == True:
                if latest_level is not None:
                    b = (float(latest_level - self.typical_range[0]) / (float(self.typical_range[1] - self.typical_range[0])))
                    return b
                elif latest_level is None:
                    return None

>>>>>>> f9b22deb9b4a41ccfc79b8a6b35c24bb77ca94c9
def inconsistent_typical_range_stations(stations):
    a = []
    for i in stations:
        j = i.typical_range_consistent()
        if j == False:
            a.append(i.name)
    return a


