from apscheduler.schedulers.blocking import BlockingScheduler
import sendtweet
from maketext import weather
import urllib.request
import urllib.error
import json
from wwebhook import to_slack
import slackweb


# スケジューラー
sched = BlockingScheduler(timezone="UTC")


#"corn",の後ろが時間の指定
@sched.scheduled_job("cron", hour=21,minute=10)
def scheduled_job():
    #2700を変えると地域が変わる
    #東京：130010 大阪：2700  など
    #http://weather.livedoor.com/ ここから自分の都道府県のページを開いて右端の数字をここに入れればできます
    text = weather('270000')
    #ツイートする
    sendtweet.tweettext(text)
    #(@channel付きで)slackに送信
    to_slack(text+'\n <!channel>')


# スケジューラー開始
sched.start()
