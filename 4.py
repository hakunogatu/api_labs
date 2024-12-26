import requests

def get_city_coordinates(city, api_key):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": city,
        "format": "json",
        "apikey": api_key,
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            geo_object = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            coordinates = geo_object["Point"]["pos"]
            lon, lat = map(float, coordinates.split())
            return lat, lon
        except (IndexError, KeyError):
            return None
    else:
        print(f"Ошибка при запросе к API: {response.status_code}")
        return None


def find_southernmost_city(cities, api_key):
    southernmost_city = None
    min_lat = float("inf")

    for city in cities:
        coordinates = get_city_coordinates(city.strip(), api_key)
        if coordinates:
            lat, _ = coordinates
            if lat < min_lat:
                min_lat = lat
                southernmost_city = city.strip()
        else:
            print(f"Не удалось получить координаты для города: {city.strip()}")

    return southernmost_city


cities_list = ["Уфа", "Мурманск", "Краснодар"]

api_key = "6d82478e-0331-49a9-a14b-3531527e55d3"

southernmost = find_southernmost_city(cities_list, api_key)

if southernmost:
    print(f"Самый южный город: {southernmost}")
else:
    print("Не удалось определить самый южный город.")
