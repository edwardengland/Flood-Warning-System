# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
from floodsystem.stationdata import build_station_list, update_water_levels

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    


    # Task 1F (EE)

    def typical_range_consistent(self):
        if self.typical_range is None:
            return False
        elif (self.typical_range[1] - self.typical_range[0]) < 0:
            return False
        else:
            return True

        # return self.typical_range is not None and self.typical_range[1] - self.typical_range[0]) >= 0


def inconsistent_typical_range_stations(stations):
    list_of_incons_stations = []  
    for i in stations:
        if i.typical_range_consistent() == False:
            list_of_incons_stations.append(i)

    return list_of_incons_stations

class MonitoringStation:

    # Task 2B 
    def relative_water_level(self):
        stations = build_station_list()
        for station in stations:
            if station is in inconsistent_typical_range_stations(stations):
                return None
            else:
                fraction_of_typical_range = (station.latest_level - station.typical_range[0])/(station.typical_range[1] - station[0])
                
    return fraction_of_typical_range
