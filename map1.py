import folium
import pandas
# use pandas to read data file
data = pandas.read_csv('Webmap_datasources/Volcanoes.txt')

# grabs values from data column and converts them to lists
lat = list(data['LAT'])
lon = list(data['LON'])
volc_name = list(data['NAME'])
# tiles gives us terrain map
map = folium.Map(location=[28.01381155418516, -82.56964496261388],tiles = "Stamen Terrain")

# By making this you have orginzation and will help when you want to add layer control feature later
fg = folium.FeatureGroup(name="My Map")

# zip merges both lists
for lt, ln in zip(lat, lon):
# add markers to map
    fg.add_child(folium.Marker(location=[lt,ln] , popup='hello there', icon=folium.Icon(color='red')))

map.add_child(fg)

map.save('Map1.html')