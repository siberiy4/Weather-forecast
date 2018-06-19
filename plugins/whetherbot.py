
import urllib.request, urllib.error
import json
from slackbot.bot import listen_to
import datetime
import time

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
			if today_max  is not "None" :
					today_max =str(temperature['max']['celsius'])
			else :
					today_max = "None"

			temperature = tomorrow['temperature']
			if temperature is not "None":
					tommorow_temperature = "   最高気温：" + str(temperature['max']['celsius']) +"   最低気温："+ str(temperature['min']['celsius'])
			else :
					tommorow_temperature = "気温 : None"

			state1=jsonfile['forecasts'][1]['telop']

		#['celsius']を入れると    
		# maxtemperature0=jsonfile['forecasts'][0]['temperature']['max']['celsius'] 
		# TypeError: 'NoneType' object is not subscriptabl
		#とでるので、できない


			text=place+"\n今日の天気："+state0+"   最高気温："+today_max+"\n明日の天気："+state1+tommorow_temperature
			#text=place+"\n今日の天気："+state0+"\n明日の天気："+state1

			message.send(text)


@listen_to('天気予報')
def prediction(massage):
		count = 0
		yestarday= 17
		while 1 :
				
				nowtime = datetime.datetime.now()
				today =int(nowtime.day)
				if today!=yestarday :
						count = 0
				if today!=yestarday :
							yestarday = today
						
				now_time_h = int(nowtime.hour)
				now_time_m = int(nowtime.minute)
				if count == 0 and 5 <= now_time_h and now_time_h<=6 and 45<=now_time_m and now_time_m<=30 :
						weather(massage)
				time.sleep(1800)




