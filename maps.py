import folium 


m = folium.Map(location = [-19.062117883514652,30.036621093749996],zoom_start = 7)
folium.Marker(location = [-19.062117883514652,30.036621093749996]).add_to(m)
m.save('map.html')