import folium
from geopy.distance import geodesic

points = [
    (55.7558, 37.6173),
    (55.715551, 37.554191),
    (55.818015, 37.440262),
    (55.791540, 37.559809)
]

path_length = 0
for i in range(len(points) - 1):
    path_length += geodesic(points[i], points[i + 1]).kilometers

mid_point_index = len(points) // 2
mid_point = points[mid_point_index]

map_center = points[0]
path_map = folium.Map(location=map_center, zoom_start=12)

folium.PolyLine(points, color="blue", weight=5, opacity=0.7).add_to(path_map)

for i, point in enumerate(points):
    folium.Marker(location=point, popup=f"Точка {i + 1}").add_to(path_map)

folium.Marker(location=mid_point, popup="Средняя точка", icon=folium.Icon(color="red")).add_to(path_map)

path_map.save("path_map.html")

print(f"Общая длина пути: {path_length:.2f} км")
print("Карта создана и сохранена в 'path_map.html'")
