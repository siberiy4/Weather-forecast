楽に天気予報が欲しかったのでpython3で作りました

TwitterとSlackで自分の都道府県の今日と明日の天気を送ります


http://toricor.hatenablog.com/entry/2017/07/17/100645

https://qiita.com/usomaru/items/529b6f40902ee1eda125

参考にしたサイト

http://weather.livedoor.com/forecast/webservice/json/v1?city=270000

読み込むjson

livedoorからjsonで天気予報をとってきます。

pipで入れるもの
〇定期実行
apscheduler
〇Twitter
twitter
〇slack
slackweb

python3 run.py
をすれば動きます

