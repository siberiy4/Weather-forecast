from slackbot.bot import listen_to
import requests


@listen_to('天気')
def weather(message):
	city_id = '2721000' # 大阪
	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=' + city_id
	data = requests.get(url).json()
	text = data['forecasts']['0']['dateLabel'].encode()
	text +=" : "
	text += data['forecasts']['0']['telop'].encode()
	text +="\n最低気温："	
	text += data['forecasts']['0']['temperature']['min']['celsius'].encode()
	text +="   最高気温："	
	text += data['forecasts']['0']['temperature']['max']['celsius'].encode()
	text +="\n"	
	message.send(text)
