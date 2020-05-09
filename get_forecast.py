import requests

# 天気情報をlivedoorから取得してくる


def get_forecast(city_id):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='

    try:
        json_data = requests.get(url + city_id).json()

        place = json_data['title']
        forecasts = json_data['forecasts']

        today = forecasts[0]
        tomorrow = forecasts[1]
        today_gif=today['image']['url']
        today_min = today['temperature']['min']['celsius']
        today_max = today['temperature']['max']['celsius']
        tomorrow_min = tomorrow['temperature']['min']['celsius']
        tomorrow_max = tomorrow['temperature']['max']['celsius']

    except:
        place = today['telop'] = today_gif = today_min = today_max = tomorrow['telop'] = tomorrow_min = tomorrow_max = None

    return place, today['telop'], today_gif, today_min, today_max, tomorrow['telop'], tomorrow_min, tomorrow_max
