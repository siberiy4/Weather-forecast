import requests

# 天気情報をlivedoorから取得してくる


def get_forecast(city_id):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='

    try:
        json_data = requests.get(url + city_id).json()
        place = json_data['title']
        forecasts = json_data['forecasts']
        today = forecasts[0] if forecasts[0] else "不明"
        tomorrow = forecasts[1] if forecasts[1] else "不明"
        today_gif = today['image']['url'] if today['image']['url'] else "不明"
        today_max = today['temperature']['max']['celsius'] if today['temperature']['max'] != None else "不明"
        tomorrow_min = tomorrow['temperature']['min']['celsius'] if tomorrow['temperature']['min'] != None else "不明"
        tomorrow_max = tomorrow['temperature']['max']['celsius'] if tomorrow['temperature']['max'] != None else "不明"
    except:
        print("err")



    return place, today['telop'], today_gif,  today_max, tomorrow['telop'], tomorrow_min, tomorrow_max
