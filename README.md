#slack-weather_forcast

Slackで自分の都道府県の今日と明日の天気を送ります

参考サイト

〇天気の取得  
http://toricor.hatenablog.com/entry/2017/07/17/100645  
https://qiita.com/usomaru/items/529b6f40902ee1eda125

〇slackへのテキストの投稿  
~https://www.cresco.co.jp/blog/entry/4139/~  
https://qiita.com/hththt/items/14bfc2bf23192b020371

〇定期実行  
https://github.com/Tosachi/Slack_weather_bot



読み込むjson

http://weather.livedoor.com/forecast/webservice/json/v1?city=270000

  
livedoorからjsonで天気予報をとってきます。  
  
```
pip3 install apscheduler 
```

pipで入れるもの  
〇定期実行  
apscheduler
  


