"""Unit test for the 1F Task"""


from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import MonitoringStation


#defines a station with no typical range data:
x = MonitoringStation('test', 'test', 'label', [0,0], None, 'river', 'town') 

def test_1f():
    """ensures the function works when there is no typical range data"""
    assert inconsistent_typical_range_stations([x]) == [x]