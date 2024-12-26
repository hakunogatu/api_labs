import requests
import math


def get_coordinates(address, api_key):
    base_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": api_key,
        "geocode": address,
        "format": "json"
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    data = response.json()
    try:
        coordinates = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        lon, lat = map(float, coordinates.split())
        return lat, lon
    except (IndexError, KeyError):
        raise ValueError("Не удалось получить координаты для адреса: " + address)


def calculate_distance(lat1, lon1, lat2, lon2):
    lat_diff = abs(lat1 - lat2) * 111
    avg_lat = math.radians((lat1 + lat2) / 2)
    lon_diff = abs(lon1 - lon2) * 111 * math.cos(avg_lat)
    return math.sqrt(lat_diff ** 2 + lon_diff ** 2)


def main():
    api_key = "6d82478e-0331-49a9-a14b-3531527e55d3"

    home_address = input("Введите адрес вашего дома: ")
    university_address = input("Введите адрес университета: ")

    try:
        home_coords = get_coordinates(home_address, api_key)
        university_coords = get_coordinates(university_address, api_key)

        distance = calculate_distance(*home_coords, *university_coords)

        print(f"Расстояние между вашим домом и университетом: {distance:.2f} км")
    except Exception as e:
        print("Произошла ошибка:", e)


main()