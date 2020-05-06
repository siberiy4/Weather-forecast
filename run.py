from apscheduler.schedulers.blocking import BlockingScheduler
from maketext import weather
import urllib.request
import urllib.error
import json



# スケジューラー
sched = BlockingScheduler(timezone="UTC")


#"corn",の後ろが時間の指定
@sched.scheduled_job("cron", hour=21,minute=10)
def scheduled_job():
    text = weather('270000')
    #(@channel付きで)slackに送信
    to_slack(text+'\n <!channel>')


# スケジューラー開始
sched.start()
