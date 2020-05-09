from get_forecast import get_forecast
import json
import requests

def post_message(webhookURL, city_id):
    place, today, today_gif, today_max, tomorrow, tomorrow_min, tomorrow_max = get_forecast(city_id)
    

    if place == None  :
        message={"text":"天気予報がわかりませんでした"}
        pass
    else:
        text = '今日の天気：{} 最高気温: {}'.format(today, today_max)
        section = text+'\n明日の天気:{} 最低気温: {} 最高気温: {}'.format(
            tomorrow, tomorrow_min, tomorrow_max)
        if today_gif == None:
            message = {"text":section}
        else:
            message = {"text": text, "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": "<!channel>\n"+section},
                                               "accessory": {"type": "image", "image_url": today_gif, "alt_text": "weather"}}]}
            pass
        pass
    
    print(message)

    requests.post(webhookURL, json.dumps(message), \
        headers={'Content-Type': 'application/json'})
