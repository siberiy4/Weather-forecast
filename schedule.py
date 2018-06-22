## 10分ごとに天気を取得し変更する。このファイルを実行する。

from apscheduler.schedulers.blocking import BlockingScheduler
from plugins import weatherbot 

# スケジューラー
sched = BlockingScheduler()

# 10の倍数分に天気を取得しそれぞれ変更する


@sched.scheduled_job("cron", hour="6")
def scheduled_job():
  weatherbot.prediction()


# スケジューラー開始
sched.start()
