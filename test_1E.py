from floodsystem.stationdata import build_station_list as stations
from floodsystem.geo import rivers_by_station_number

def test_1E():
    #Task 1E Produce a list with the N rivers having the greatest number of monitoring stations (SZ)

    def rivers_by_station_number(stations, N):
        """returns first N rivers with highest # stations /river. if rivers have the same number of stations at end of list, all stations with this number of stations are also returned, as well as # of stations."""
        list_of_rivers_by_stations_w_dup = []
        list_of_rivers = []

        for i in stations:
            list_of_rivers += [i.river]  #produces a list of rivers for each station, this will return duplicates of a river within the list

        for i in list_of_rivers:
            list_of_rivers_by_stations_w_dup += [(i, list_of_rivers.count(i))] #produces a list of rivers with the number of stations it has, will have duplicates within list
        

        list_of_rivers_by_stations = set(list_of_rivers_by_stations_w_dup) #gets rid of the duplicates

        sorted_list_of_rivers_by_stations = sorted_by_key(list_of_rivers_by_stations, 1, reverse = True) #changes the list to put the rivers in descending order of how many stations they have
    
        assert type(sorted_list_of_rivers_by_stations) == type(set)
        output = []
        output.append(sorted_list_of_rivers_by_stations[0:N]) #produces initial list of the first N rivers with the highest number of stations

        x=N
        counter = 0
        while counter in range(999):
            if sorted_list_of_rivers_by_stations[x-1][1] == sorted_list_of_rivers_by_stations[x][1]:
                output.append(sorted_list_of_rivers_by_stations[x])
                x += 1
                counter += 1 #adds extra rivers if the last river isn't the only one with its number of stations
            else:
                counter = 999
            
        
        return output 