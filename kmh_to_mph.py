distance_in_km = int(input(150))
time_in_hours = int(input(2))
distance_in_mi = distance_in_km / 1.6
distance_in_mtrs = distance_in_km * 1000
speed_in_kph = distance_in_km / time_in_hours
speed_in_mph = distance_in_mi / time_in_hours
print ("Speed in kilometers per hour:", speed_in_kph, "and miles per hour:", speed_in_mph)