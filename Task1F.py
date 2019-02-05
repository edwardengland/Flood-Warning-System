# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    listy = inconsistent_typical_range_stations(stations)

    output = []
    # takes just the name of the stations.
    for i in listy:
            output.append(i.name)

    print( sorted(output))




if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
