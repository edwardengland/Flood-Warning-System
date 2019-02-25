from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.utils import sorted_by_key
stations = build_station_list()

def stations_level_over_threshold(stations, tol):
    s_l_o_t = []
    for station in stations:
        if station.relative_water_level > tol:
            s_l_o_t += (station, station.relative_water_level)
    return sorted_by_key(s_l_o_t, 1, reverse=True)



