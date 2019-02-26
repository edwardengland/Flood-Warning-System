import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()
for i in stations: 
    dt = 10
    dates, levels = fetch_measure_levels(i[0].measure_id, dt = datetime.timedelta(days = dt))

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    p_coeff = np.polyfit(x, y, p)
    plt.plot(x, y, '.')

