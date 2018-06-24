import urllib.request
import urllib.error
import json

#天気情報をlivedoorから取得してくる

def weather(city_id):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    data = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(data.read().decode('utf-8'))
    place=jsonfile['title']
    state0=jsonfile['forecasts'][0]['telop']
    forecasts = jsonfile['forecasts']

    today = forecasts[0]
    tomorrow=forecasts[1]
    temperature = today['temperature']
    today_max =str(temperature['max'])

    today_max =str(temperature['max']['celsius'])


    temperature = tomorrow['temperature']

    tommorow_temperature = "   最高気温 ： " + str(temperature['max']['celsius']) +"   最低気温 ： "+ str(temperature['min']['celsius'])

    state1=jsonfile['forecasts'][1]['telop']



    text=place+"\n\n今日の天気 ： "+state0+"   最高気温 ： "+today_max+"\n明日の天気 ： "+state1+tommorow_temperature

    return text
