import requests


def get_weather_desc_temp():
    api_key = "d948299d7f4501ab128c5242558227b9"
    city = "Lagos"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key + "&units=imperial"
    request = requests.get(url)
    json = request.json()
    # print(json)
    description = json.get('weather')[0].get('description')
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}


weather_dict = get_weather_desc_temp()

print("Today's forecast is", weather_dict.get('description'))
print("The minimum temperature today is ", weather_dict.get('temp_min'))
print("The maximum temperature today is ", weather_dict.get('temp_max'))
