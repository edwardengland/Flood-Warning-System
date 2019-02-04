# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine

# Task 1B: Sort Stations by distance  (EE)
from floodsystem.utils import *

def stations_by_distance(stations, p):
    """Takes a list of stations and a co-ordinate, returns a list of tuples sorted by distance"""
    list_of_tuples = []
    
    for i in stations:
        list_of_tuples.append((i, haversine(i.coord, p)))
 
    return sorted_by_key(list_of_tuples, 1)



#Task 1C Produce a function which returns stations within a certain radius of a coordinate  (SZ)

def stations_within_radius(stations, centre, r):
    """takes station object list, a set of coordinates and a distance.
    returns a list of stations within that distance away from the set of coordinates. """
    stations_within_r_of_x = []
    for i in stations:
        distance_station_centre = haversine(i.coord, centre)
        if distance_station_centre <= r:
            stations_within_r_of_x.append(i)

    return(stations_within_r_of_x)





#Task 1D (1)  Produce a list of rivers with stations without reiteration and in alphabetical order (SZ)

def rivers_with_station(stations):
    """takes station object list.
      returns a set of rivers which have stations."""
    set_rivers = set()
    for i in stations:
        set_rivers.add(i.river)
    
    return sorted(set_rivers)

# Task 1D (2)       (EE)

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

#Task 1E Produce a list with the N rivers having the greatest number of monitoring stations

def rivers_by_station_number(stations, N):
    list_of_rivers_by_station_number = []
    
    
