import requests

def get_coordinates(address, api_key):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": address,
        "format": "json",
        "apikey": api_key,
    }
    response = requests.get(geocode_url, params=params)
    response.raise_for_status()

    data = response.json()
    try:
        point = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
        lon, lat = point.split()
        return lat, lon
    except (KeyError, IndexError):
        print("Ошибка: Не удалось найти координаты по указанному адресу.")
        exit(1)


def get_district(lat, lon, api_key):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "geocode": f"{lon},{lat}",
        "format": "json",
        "apikey": api_key,
        "kind": "district",
    }
    response = requests.get(geocode_url, params=params)
    response.raise_for_status()

    data = response.json()
    try:
        district = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["name"]
        return district
    except (KeyError, IndexError):
        print("Ошибка: Не удалось определить район для указанных координат.")
        exit(1)


address = input("Введите адрес: ")
api_key = "6d82478e-0331-49a9-a14b-3531527e55d3"

lat, lon = get_coordinates(address, api_key)
district = get_district(lat, lon, api_key)

print(f"Район для адреса '{address}': {district}")
