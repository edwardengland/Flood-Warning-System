from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta


def run():

    stations = build_station_list()

    today = datetime.

    top_5 = stations_highest_rel_level(stations, 5)
    dates = []
    for i in top_5:
        plot_water_levels(i), dates, levels)