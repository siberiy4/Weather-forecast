from get_forecast import get_forecast

import requests

def post_message(webhookURL, city_id):
    place, today, today_gif, today_max, tomorrow, tomorrow_min, tomorrow_max = get_forecast(city_id)
    
    if place == None or today==None :
        message='{"text":"天気予報がわかりませんでした"}'
        pass
    else:
        text = '今日の天気：{} 最高気温: {}'.format(today, today_max)
        section = text+'\n明日の天気:{} 最低気温: {} 最高気温: {}'.format(
            tomorrow, tomorrow_min, tomorrow_max)
        if today_gif == None:
            message = '{"text":"{}"}'.format(section)
        else:
            message = '{"text":"{}","blocks": [{"type": "section","text": {"type": "mrkdwn","text": "<!channel>\n{}"},\
                "accessory": {"type": "image","image_url": "{}","alt_text": "weather"}}]}'.format(text, section, today_gif)
            pass
        pass

    response = requests.post(webhookURL, message, \
        headers={'Content-Type': 'application/json'})
    print(response)
