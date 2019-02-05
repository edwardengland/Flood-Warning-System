from floodsystem.stationdata import build_station_list as stations
from haversine import haversine

def test_1C():
    def stations_within_radius(stations, centre, r):
        stations_within_r_of_x = []
        for i in stations:
            distance_station_centre = haversine(i.coord, centre)
        if distance_station_centre <= r:
            stations_within_r_of_x.append(i)
    
        assert len(distance_station_centre) == len(stations)
        return(stations_within_r_of_x)
