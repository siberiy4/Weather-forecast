楽に天気予報が欲しかったのでpython3で作りました

TwitterとSlackで自分の都道府県の今日と明日の天気を送ります

参考サイト

〇天気の取得  
http://toricor.hatenablog.com/entry/2017/07/17/100645  
https://qiita.com/usomaru/items/529b6f40902ee1eda125

〇slackへのテキストの投稿  
https://www.cresco.co.jp/blog/entry/4139/

〇定期実行  
https://github.com/Tosachi/Slack_weather_bot



読み込むjson

http://weather.livedoor.com/forecast/webservice/json/v1?city=270000

  
livedoorからjsonで天気予報をとってきます。  
  
```
pip3 install apscheduler twitter slackweb  
```

pipで入れるもの  
〇定期実行  
apscheduler
  
〇Twitter  
twitter  
  
〇slack  
slackweb  

python3 run.py
をすれば動きます

