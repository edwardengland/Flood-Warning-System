from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()

for station in stations:
    print(station.relative_water_level)
