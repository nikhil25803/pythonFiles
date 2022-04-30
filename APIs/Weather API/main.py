import requests
import json

# city_name = input("Enter the city name: ")

# URL = "https://api.openweathermap.org/data/2.5/weather?q=Patna&appid=01019b2042882a4a2cb94669f5e36552"
# r = requests.get(url=URL)
# data = r.json()
# json_write = json.dumps(data, indent=4)
# temp = data["main"]["temp_max"]
# print(json_write)
# with open("json_file.json", "w") as f:
#     data = json.load(f)

def weather(name):

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid=01019b2042882a4a2cb94669f5e36552"

    r = requests.get(url=api_url)
    data = r.json()
    json_write = json.dumps(data, indent=4)

    with open("json_file.json", "w") as f:
        f.write(json_write)
    # print(json_write)

weather("Patna")


with open("json_file.json", "r") as r:

    data = json.load(r)

print(data["name"])
