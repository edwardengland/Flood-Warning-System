from floodsystem.geo import stations_within_radius


# look at stations which have a water level above the typical high.
# find which town station is in.
# what proportion of stations near (within 1km radius?) are predicting a flood

list_over_1 = []

for i in stations:
    if i.relative_water_level() >= 1:
        list_over_1.append(i)


for i in list_over_1:
    all_near_stations =  stations_within_radius(stations, i.coord, 1)
    near_stations_over_1 = stations_within_radius(list_over_1, i.coord, 1)
    proportion = len(near_stations_over_1)/len(all_near_stations)

if proportion >= 0.7:
