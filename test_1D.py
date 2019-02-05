from floodsystem.stationdata import build_station_list as stations

def test_1D():
    #Task 1D (1)  Produce a list of rivers with stations without reiteration and in alphabetical order (SZ)

    def rivers_with_station(stations):
        """takes station object list.
        returns a set of rivers which have stations."""
        set_rivers = set()
        for i in stations:
            set_rivers.add(i.river)
        assert type(set_rivers) == type(set)
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
        assert type(stations_by_river_dictionary) == type(dict)
        return stations_by_river_dictionary
        

