from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():

    stations = build_station_list()
    update_water_levels(stations)
        

    top_5 = stations_highest_rel_level(stations, 5)

    for i in top_5:
        times = []
        levels_list = [] 
        dt = 10
        dates, levels = fetch_measure_levels(i[0].measure_id, dt = datetime.timedelta(days = dt))

        for date, level in zip(dates, levels):
                times.append(date)
                levels_list.append(level)

        plot_water_levels(i[0], times, levels_list)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()