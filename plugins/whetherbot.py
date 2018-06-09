
import urllib.request, urllib.error
import json
from slackbot.bot import listen_to

@listen_to('天気')
def weather(message):


	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city='
	# '130010'とすると東京の情報を取得してくれる
	# ここを変えれば任意の地域の天気情報を取得できる
	city_id = '270000'
	data = urllib.request.urlopen(url + city_id)
	jsonfile = json.loads(data.read().decode('utf-8'))
	place=jsonfile['title']
	state0=jsonfile['forecasts'][0]['telop']
	forecasts = jsonfile['forecasts']
	today = forecasts[0]
	tomorrow=forecasts[1]
	temperature = today['temperature']
	today_max =str(temperature['max'])	
	if today_max  is  None :
		today_max =str(temperature['max']['celsius'])
	
	temperature = tomorrow['temperature']
	tommorow_max = str(temperature['max']['celsius'])	
	tommorow_min = str(temperature['min']['celsius'])

	state1=jsonfile['forecasts'][1]['telop']

#['celsius']を入れると    
# maxtemperature0=jsonfile['forecasts'][0]['temperature']['max']['celsius'] 
# TypeError: 'NoneType' object is not subscriptabl
#とでるので、できない


	text=place+"\n今日の天気："+state0+"   最高気温："+today_max+"\n明日の天気："+state1+"   最高気温："+tommorow_max+"   最低気温："+tommorow_min
	#text=place+"\n今日の天気："+state0+"\n明日の天気："+state1

	message.send(text) 


