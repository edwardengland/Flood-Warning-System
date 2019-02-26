from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit

import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
    
    plt.plot(dates, levels)

    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    typ_high = [station.typical_range[1]]
    typ_low = [station.typical_range[0]]

    plt.plot([dates[0], dates[-1]], [typ_high, typ_high])
    plt.plot([dates[0], dates[-1]], [typ_low, typ_low])

    plt.tight_layout()
    plt.show()

#Task 2F

def plot_water_level_with_fit(stations, dates, levels, p):
