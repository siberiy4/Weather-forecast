import requests
import json

def post_message(webhookURL):
    response = requests.post(webhookURL, json.dumps({'text': 'test'}), \
        headers={'Content-Type': 'application/json'})
    print(response)
