from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from haversine import haversine

def run():
    """Requirements for Task 1C"""


     # Build list of stations
    stations = build_station_list()

    centre = (52.2053, 0.1218) #Cambridge city centre
    r= 10.0 #set radius to 10km

    print(stations_within_radius(stations, centre, r))

    for i in stations_within_radius(stations, centre, r):
        print(sorted(i.name)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()