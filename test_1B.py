"""Unit test for the 1B Task"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

stations = build_station_list()

def test_1b():
    """Test checks that the output is the correct type"""
    x = stations_by_distance(stations, (50,0.1))

    assert type(x)==list

