import requests
import random
from io import BytesIO
from PIL import Image

# Константы
YANDEX_API_KEY = "853dcde5-7ffc-4e23-81f7-81878d1cfcd5"
BASE_URL = "https://static-maps.yandex.ru/1.x/"
CITY_LIST = ["Москва", "Санкт-Петербург", "Казань", "Новосибирск", "Екатеринбург"]


def get_city_image(city_name):
    city_coordinates = {
        "Москва": "55.7558,37.6173",
        "Санкт-Петербург": "59.9343,30.3351",
        "Казань": "55.796127,49.106414",
        "Новосибирск": "55.0084,82.9357",
        "Екатеринбург": "56.8389,60.6057"
    }

    coords = city_coordinates[city_name]

    zoom = 15
    size = "450,450"  # Уменьшили размер
    map_type = random.choice(["map", "sat", "sat,skl"])

    params = {
        "ll": coords,
        "z": zoom,
        "size": size,
        "l": map_type,
        "key": YANDEX_API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    return Image.open(BytesIO(response.content))


random.shuffle(CITY_LIST)

for city in CITY_LIST:
    print(f"Показываем карту города: {city} (ответ держим в секрете)")

    try:
        image = get_city_image(city)
        image.show()
    except Exception as e:
        print(f"Ошибка при загрузке карты для города {city}: {e}")

    input("Нажмите Enter, чтобы перейти к следующему городу...")
