import requests

api_key = "6d82478e-0331-49a9-a14b-3531527e55d3"

def get_satellite_image(coords, output_file="satellite_image.png"):
    url = "https://static-maps.yandex.ru/1.x/"
    params = {
        "ll": f"{coords[1]},{coords[0]}",
        "z": 16,
        "size": "650,450",
        "l": "sat",
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Снимок сохранён: {output_file}")
    else:
        print("Не удалось получить снимок.")


get_satellite_image((55.715551, 37.554191))