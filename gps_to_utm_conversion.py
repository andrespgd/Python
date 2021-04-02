import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import utm
import sys

fname = 'gps_to_utm_conversion.csv'
df_original = pd.read_csv(fname)

df = df_original.dropna()

# method1 - single values
dic1 = {'east':[], 'north':[], 'zone_n':[], 'zone_l':[]}
for index, row in df.iterrows():
    EASTING, NORTHING, ZONE_NUMBER, ZONE_LETTER = utm.from_latlon(row['gps_Latitude'], row['gps_Longitude'])
    dic1['east'].append(EASTING)
    dic1['north'].append(NORTHING)
    dic1['zone_n'].append(ZONE_NUMBER)
    dic1['zone_l'].append(ZONE_LETTER)
df['east'] = dic1['east'] 
df['north'] = dic1['north'] 
    
# method2 - mutiple values
# ZONE_NUMBER and ZONE_LETTER are scalars and will be calculated for the first point of the input. 
# All other points will be set into the same UTM zone. 

e,n,zn,zl = utm.from_latlon(df['gps_Latitude'].to_numpy(), df['gps_Longitude'].to_numpy())
df['east'] = e
df['north'] = n

# plot trajectory in local coordinates with speed
fig, ax = plt.subplots(1, 1)
ax.plot(df['east'], df['north'])
ax.set_aspect('equal')
ax.set_xlabel('easting')
ax.set_ylabel('northing')
for i in np.arange(0,df.shape[0],100):
    ax.text(df['east'].iloc[i], df['north'].iloc[i], str(int(df['gps_Speed'].iloc[i]))+'mph')
plt.show()


import folium
import webbrowser

centroid_lat = df['gps_Latitude'].mean()
centroid_lon = df['gps_Longitude'].mean()

m = folium.Map([centroid_lat, centroid_lon], zoom_start=14)

for ix, row in df.iterrows():
    folium.CircleMarker([row['gps_Latitude'], row['gps_Longitude']],radius=5,fill_color='blue').add_to(m)
 
fname_out = os.path.splitext(os.path.basename(sys.argv[0]))[0]
m.save(fname_out+'.html')
webbrowser.open(fname_out+'.html')


