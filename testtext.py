import urllib.request
import urllib.error
import json


def weather(city_id):
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
    data = urllib.request.urlopen(url + city_id)
    jsonfile = json.loads(data.read().decode('utf-8'))
    place=jsonfile['title']
    state0=jsonfile['forecasts'][0]['telop']
    state1=jsonfile['forecasts'][1]['telop']



    text=place+"\n\n今日の天気 ： "+state0+"\n明日の天気 ： "+state1
    return text
