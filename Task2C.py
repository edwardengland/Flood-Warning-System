from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level




def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    for i in range(10):
        print(stations_highest_rel_level(stations, 10)[i][0].name,stations_highest_rel_level(stations, 10)[i][0].relative_water_level())


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()