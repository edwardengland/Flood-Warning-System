
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # Part 1 of task 1D (SZ)
    print(rivers_with_station(stations)[0:10])

    # Part 2 of task 1D (EE)
    # Print names of stations on a given river in alpha. order
    stations_by_river_dictionary= stations_by_river(stations)
    
    
    # creates a list to add to
    stations_on_aire = []
    
    # takes stations from dictionary
    list_of_stations_aire = stations_by_river_dictionary["River Aire"]
    
    # adds just the name of the station to the list and sorts
    for i in list_of_stations_aire:
        stations_on_aire.append(i.name)
    stations_on_aire.sort()
    print(stations_on_aire)

    print()

    stations_on_cam = []
    list_of_stations_cam = stations_by_river_dictionary["River Cam"]
    for i in list_of_stations_cam:
        stations_on_cam.append(i.name)
    stations_on_cam.sort()
    print(stations_on_cam)

    print()

    stations_on_thames = []
    list_of_stations_thames = stations_by_river_dictionary["River Thames"]
    for i in list_of_stations_thames:
        stations_on_thames.append(i.name)
    stations_on_thames.sort()
    print(stations_on_thames)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()