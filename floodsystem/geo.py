# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#Task 1C Produce a function which returns stations within a certain radius of a coordinate
from haversine import haversine

def stations_within_radius(stations, centre, r):
    stations_within_r_of_x = []
    for i in stations:
        distance_station_centre = haversine(i.coord, centre)
        if distance_station_centre <= r:
            stations_within_r_of_x.append(i.name)

    return(sorted(stations_within_r_of_x))





#Task 1D (1)  Produce a list of rivers with stations without reiteration and in alphabetical order

def rivers_with_station(stations):
    """takes station object list.
      returns a set of rivers which have stations."""
    set_rivers = set()
    for i in stations:
        set_rivers.add(i.river)
    
    return sorted(set_rivers)

# Task 1D (2)

def stations_by_river(stations):
    """takes list of station objects
        returns dictionary of format {river: list of stations on this river}"""
   
    stations_by_river_dictionary = {}
    
    # if station is in dictionary, add to to appropriate list, else create new key and item
    for object in stations:
        if object.river in stations_by_river_dictionary:
            stations_by_river_dictionary[object.river].append(object)
        else:
            stations_by_river_dictionary[object.river] = [object]
    return stations_by_river_dictionary
