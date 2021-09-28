import folium
# tiles gives us terrain map
map = folium.Map(location=[28.01381155418516, -82.56964496261388],tiles = "Stamen Terrain")

# By making this you have orginzation and will help when you want to add layer control feature later
fg = folium.FeatureGroup(name="My Map")

# add markers to map
fg.add_child(folium.Marker(location=[28.01381155418516, -82.56964496261388], popup='Hey there im a marker', icon=folium.Icon(color='green')))

map.add_child(fg)

map.save('Map1.html')