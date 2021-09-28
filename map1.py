import folium
# tiles gives us terrain map
map = folium.Map(location=[28.01381155418516, -82.56964496261388],tiles = "Stamen Terrain")

# add markers to map
map.add_child(folium.Marker(location=[28.01381155418516, -82.56964496261388], popup='Hey there im a marker', icon=folium.Icon(color='green')))

map.save('Map1.html')