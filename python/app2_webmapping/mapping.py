# mapping with the folium package
import folium

# pass a geo location (i chose dodger stadium)
map = folium.Map(location=[34.073922, -118.239518])

# add zoom parameter (higher to zoom in)
map = folium.Map(location=[34.073922, -118.239518], zoom_start=17)

# add tiles
map = folium.Map(location=[34.073922, -118.239518], zoom_start=17, tiles="Mapbox Bright")

# create a feature group to add elements
fg = folium.FeatureGroup(name="My Custom Map")

# add elements to Map object
fg.add_child(folium.Marker(location=[34.1, -118.3], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

# save to html
map.save("Map1.html")
