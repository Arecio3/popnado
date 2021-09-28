import folium
from folium.map import LayerControl
import pandas
# use pandas to read data file
data = pandas.read_csv('Webmap_datasources/Volcanoes.txt')

# By making this you have orginzation and will help when you want to add layer control feature later
fgv = folium.FeatureGroup(name="Volcanoes")
fg = folium.FeatureGroup(name="Population")

# grabs values from data column and converts them to lists
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
volc_name = list(data['NAME'])
# string of html for link and info
html = """
<div class="volc_info">
<b>Volcano name:</b><br>
<a href="https://www.google.com/search?q=%%22%s%%22volcano" id="volc_link" target="_blank">%s</a><br>
Height: %s m </div>
"""

# tiles gives us terrain map
map = folium.Map(location=[28.01381155418516, -82.56964496261388],tiles = "Stamen Terrain", zoom_start=5)

# check elevation
def elevation(elev):
        if elev < 1500:
            return 'green'
        elif elev >= 1500 and elev < 2500:
            return 'orange'
        else:
            return 'red'

# zip merges lists
for lt, ln, el, volc in zip(lat, lon, elev, volc_name):
    # iframe is for adding html
    iframe = folium.IFrame(html=html % (volc, volc, el), width=200, height=100)
    # add markers to map
    fgv.add_child(folium.Marker(location=[lt,ln] , popup=folium.Popup(iframe), icon=folium.Icon(color=elevation(el), icon="glyphicon-fire")))

# polgon layer with color check for pop
fg.add_child(folium.GeoJson(data=open('Webmap_datasources/world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 100000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# Adds volcano features
map.add_child(fgv)
# Adds population features
map.add_child(fg)

# Layer controller (THIS MUST BE AFTER LINE 48 or it wont find the layers)
map.add_child(folium.LayerControl())

map.save('Map1.html')