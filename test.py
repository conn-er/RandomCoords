from folium import plugins, Map, Circle, CircleMarker, PolyLine
from randomcoords import RandomCoords


center_point = [34.062400, -117.894900]  # Defining the center of our map as well as our RandomCoords objects

# Making our first map, a 100km circle with 5000 points.
map1 = Map(location=center_point, zoom_start=12)

rc = RandomCoords(center=center_point, diameter=100, units='km')
for point in rc.generate_coords(num_coords=5000):
    CircleMarker(location=point, radius=2, color='blue').add_to(map1)

Circle(radius=50000, location=center_point, fill=False, color='red').add_to(map1)

map1.save(r'C:\Users\User\Desktop\big_map_km.html')


# Making our second map, a 10mi circle with 500 points.
map2 = Map(location=center_point, zoom_start=12)

rc2 = RandomCoords(center=center_point, diameter=10, units='mi')
for point in rc2.generate_coords(num_coords=500):
    CircleMarker(location=point, radius=2, color='blue').add_to(map2)

Circle(radius=8046, location=center_point, fill=False, color='red').add_to(map2)

map2.save(r'C:\Users\User\Desktop\smaller_map_mi.html')


# Making our third map, a 52,800ft circle with 500 points represented as a heat map.
rc3 = RandomCoords(center=center_point, diameter=52800, units='ft')

map3 = Map(location=center_point, zoom_start=12)

plugins.HeatMap(data=rc3.generate_coords(num_coords=500)).add_to(map3)

Circle(radius=8046, location=center_point, fill=False, color='red').add_to(map3)

map3.save(r'C:\Users\User\Desktop\smaller_heat_map_ft.html')


# Making a map using generate_paths.
map4 = Map(location=center_point, zoom_start=12)

rc4 = RandomCoords(center=center_point, diameter=10, units='km')

for path in rc4.generate_paths(num_paths=15, num_points_range=(10, 50), circle_radius_range=(15, 25)):
    for point in path:
        CircleMarker(location=point, radius=2, color='blue', fill=True, fill_opacity=1).add_to(map4)
    PolyLine(locations=path, color='blue', weight=1).add_to(map4)

Circle(radius=5000, location=center_point, fill=False, color='red').add_to(map4)

map4.save(r'C:\Users\User\Desktop\path_map_km.html')


# Printing out the output for our RandomCoords objects as well as some sample output of the generate_coords function.
print('Object \'rc\' __str__ returns:')
print(rc, '\n')
print('Object \'rc2\' __str__ returns:')
print(rc2, '\n')
print('Object \'rc3\' __str__ returns:')
print(rc3, '\n')
print('Object \'rc4\' __str__ returns:')
print(rc4, '\n')

print('rc.generate_coords(num_coords=5) returns:')
print(rc.generate_coords(num_coords=5), '\n')
print('rc2.generate_coords(num_coords=5) returns:')
print(rc2.generate_coords(num_coords=5), '\n')
print('rc3.generate_coords(num_coords=5) returns:')
print(rc3.generate_coords(num_coords=5), '\n')
print('rc4.generate_paths(num_paths=2, num_points_range=(10, 50), circle_radius_range=(15, 25)) returns:')
print(rc4.generate_paths(num_paths=2, num_points_range=(10, 50), circle_radius_range=(15, 25)), '\n')
