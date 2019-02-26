import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels

def polyfit(dates, levels, p):
    # function returns tuple of (polynomial, shift of time axis)
 
    x = matplotlib.dates.date2num(dates)
    y = levels

    p_coeff = np.polyfit(x-x[0], y, p)
    
    poly = np.poly1d(p_coeff)
    
    return (poly, x[0])