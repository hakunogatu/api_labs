import requests


def get_coordinates(address, api_key):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": address,
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
            print("Не удалось найти координаты для указанного адреса.")
            return None
    else:
        print(f"Ошибка при запросе к Геокодеру: {response.status_code}")
        return None


def find_nearest_pharmacy(lat, lon, api_key):
    url = "https://search-maps.yandex.ru/v1/"
    params = {
        "apikey": api_key,
        "text": "аптека",
        "ll": f"{lon},{lat}",
        "type": "biz",
        "lang": "ru_RU",
        "results": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        try:
            organization = response.json()["features"][0]
            name = organization["properties"]["CompanyMetaData"]["name"]
            address = organization["properties"]["CompanyMetaData"]["address"]
            return name, address
        except (IndexError, KeyError):
            print("Не удалось найти аптеки поблизости.")
            return None
    else:
        print(f"Ошибка при запросе к API поиска организаций: {response.status_code}")
        return None


user_address = input("Введите адрес: ")

geocoder_api_key = "6d82478e-0331-49a9-a14b-3531527e55d3"
search_api_key = "5d411b61-d43d-46e4-b24c-a62553d41bbb"

coordinates = get_coordinates(user_address, geocoder_api_key)
if coordinates:
    latitude, longitude = coordinates

    pharmacy = find_nearest_pharmacy(latitude, longitude, search_api_key)
    if pharmacy:
        print(f"Ближайшая аптека: {pharmacy[0]}")
        print(f"Адрес аптеки: {pharmacy[1]}")
    else:
        print("Не удалось найти ближайшую аптеку.")
