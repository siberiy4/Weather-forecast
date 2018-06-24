import slackweb
#webhookのURLを""の間に入れる"
WEBHOOK_URL = "ここ"
slack = slackweb.Slack(url=WEBHOOK_URL)

#Slackに送信
def to_slack(text: str):
    slack.notify(text=text)
