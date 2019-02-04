from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

from floodsystem.utils import sorted_by_key

def run():
    # Build list of stations
    stations = build_station_list()    
    
    output = []
    for x in stations_by_distance(stations, (52.2053, 0.1218)):
        output.append((x[0].name, x[0].town, x[1]))
    
    print("Closest 10 entries: \t" + str(output[:9]))
    print("\nFurthest 10 entries: \t" + str(output[-10:]))

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
