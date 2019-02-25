from floodsystem.stationdata import build_station_list, update_water_levels

class MonitoringStation:
    def relative_water_level(self):
        stations = build_station_list()
        for station in stations:
            fraction_of_typical_range = (station.latest_level - station.typical_range[0])/(station.typical_range[1] - station[0])
        return fraction_of_typical_range





