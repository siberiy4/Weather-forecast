from slackbot.bot import listen_to
import requests


@listen_to('天気')
def weather(message):
    city_id = '270000' # 大阪
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=' + city_id
    data = requests.get(url).json()
    text = data['description']['text'].encode()
    message.send(text)
