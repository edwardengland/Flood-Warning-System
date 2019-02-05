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

#Task 1E Produce a list with the N rivers having the greatest number of monitoring stations (SZ)

def rivers_by_station_number(stations, N):
    """returns first N rivers with highest # stations /river. if rivers have the same number of stations at end of list, all stations with this number of stations are also returned, as well as # of stations."""
    list_of_rivers_by_stations_w_dup = []
    list_of_rivers = []

    for i in stations:
        list_of_rivers += [i.river]  #produces a list of rivers for each station, this will return duplicates of a river within the list

    for i in list_of_rivers:
        list_of_rivers_by_stations_w_dup += [(i, list_of_rivers.count(i))] #produces a list of rivers with the number of stations it has, will have duplicates within list
        

    list_of_rivers_by_stations = set(list_of_rivers_by_stations_w_dup) #gets rid of the duplicates

    sorted_list_of_rivers_by_stations = sorted_by_key(list_of_rivers_by_stations, 1, reverse = True) #changes the list to put the rivers in descending order of how many stations they have
    
    output = []
    output.append(sorted_list_of_rivers_by_stations[0:N]) #produces initial list of the first N rivers with the highest number of stations

    x=N
    counter = 0
    while counter in range(999):
        if sorted_list_of_rivers_by_stations[x-1][1] == sorted_list_of_rivers_by_stations[x][1]:
            output.append(sorted_list_of_rivers_by_stations[x])
            x += 1
            counter += 1 #adds extra rivers if the last river isn't the only one with its number of stations
        else:
            counter = 999
            
        
    return output 


        


