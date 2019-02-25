from floodsystem.stationdata import build_station_list

stations = build_station_list()



def run():
    for i in stations_highest_rel_level(stations, 10):
        print(i(0).name)
        print(" ")
        print(i(1))
        print(\n)
