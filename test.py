import requests


def main():
	city_id = '2721000' # 大阪
	url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=' + city_id
	data = requests.get(url).json
	print(requests.get(url))
	print(data['forecasts'])
