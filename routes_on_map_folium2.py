import folium
import numpy as np
import webbrowser

m = folium.Map(location=[37.7954, -122.394], zoom_start=13)
tooltip = "Click me!"
folium.Marker([37.7954, -122.394], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip).add_to(m)
folium.Marker([37.7766, -122.396], popup="<b>Timberline Lodge</b>", tooltip=tooltip).add_to(m)
m.save('index1.html')
webbrowser.open('index1.html')



m = folium.Map((0.5, 0.5), zoom_start=8, tiles=None)
from folium.plugins import HeatMap
HeatMap(
# make five dots with different weights: 1, 2, 3, 4 and 5
data=[(0  , 0, 0.1),
      (0.5, 0, 0.2),
      (1.0, 0, 0.3),
      (1.5, 0, 0.4),
      (2.0, 0, 0.5)] , radius=25, blur = 10, min_opacity = 0, max_val = 0.0005).add_to(m)
m.save('index2.html')
webbrowser.open('index2.html')

lon, lat = -86.276, 30.935 
zoom_start = 5
data = (np.random.normal(size=(100, 3)) * np.array([[1, 1, 1]]) + np.array([[48, 5, 1]])).tolist()
m = folium.Map([48, 5], tiles='stamentoner', zoom_start=6)
from folium.plugins import HeatMap
HeatMap(data).add_to(m)
m.save('index3.html')
webbrowser.open('index3.html')


map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, tiles='Stamen Terrain')
folium.Marker([45.3300, -121.6823], popup='loc', icon=folium.Icon(color='red',icon='bicycle', prefix='fa')).add_to(map_1)
map_1.save('index4.html')
webbrowser.open('index4.html')