from apscheduler.schedulers.blocking import BlockingScheduler
from post_message import post_message
from dotenv import load_dotenv
import os

# 同じディレクトリにある.envファイルを読み込む
load_dotenv(verbose=True)

# 環境変数から受け取る
webhookURL = os.environ['WEB_HOOK_URL']
city_id = os.environ['CITY_ID']
ope_hour = os.environ['HOUR']
ope_minutes = os.environ['MINUTES']

# スケジューラーの準備
sched = BlockingScheduler(timezone="Asia/Tokyo")

#毎日指定の時刻に動かす
@sched.scheduled_job("cron", hour=ope_hour,minute=ope_minutes)
def scheduled_job():
    post_message(webhookURL, city_id)

# スケジューラー開始
sched.start()
