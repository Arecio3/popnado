import folium
import pandas
# use pandas to read data file
data = pandas.read_csv('Webmap_datasources/Volcanoes.txt')

# By making this you have orginzation and will help when you want to add layer control feature later
fg = folium.FeatureGroup(name="My Map")

# grabs values from data column and converts them to lists
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
volc_name = list(data['NAME'])

html = """
<b>Volcano name:</b><br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# tiles gives us terrain map
map = folium.Map(location=[28.01381155418516, -82.56964496261388],tiles = "Stamen Terrain", zoom_start=5)

# zip merges lists
for lt, ln, el, volc in zip(lat, lon, elev, volc_name):
    iframe = folium.IFrame(html=html % (volc, volc, el), width=200, height=100)
    # add markers to map
    fg.add_child(folium.Marker(location=[lt,ln] , popup=folium.Popup(iframe), icon=folium.Icon(color='red', icon="glyphicon-fire")))

map.add_child(fg)

map.save('Map1.html')