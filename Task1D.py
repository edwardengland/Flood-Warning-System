
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    # part 1 of task 1D
    print("Number of stations: {}".format(len(stations)))

    # Part 2 of task 1D
    # Print names of stations on a given river in alpha. order
    stations_by_river_dictionary= stations_by_river(stations)
    
    
    
    stations_on_aire = []
    list_of_stations_aire = stations_by_river_dictionary["River Aire"]
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