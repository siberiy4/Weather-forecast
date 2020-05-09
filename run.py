from apscheduler.schedulers.blocking import BlockingScheduler
from post_message import post_message
from dotenv import load_dotenv
import os

# 同じディレクトリにある.envファイルを読み込む
load_dotenv(verbose=True)

# 環境変数から受け取る
webhookURL = os.environ['WEB_HOOK_URL']
city_id = os.environ['CITY_ID']

post_message(webhookURL, city_id)


'''
# スケジューラー
sched = BlockingScheduler(timezone="Asia/Tokyo")

#"corn",の後ろが時間の指定
@sched.scheduled_job("cron", hour=6)
def scheduled_job():
    text = weather('270000')



# スケジューラー開始
sched.start()
'''
