#codig: UTF-8
#Twitterの送るやつ

import twitter
import sys, codecs

def tweettext(text):
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

    #Twitterの認証
    auth = twitter.OAuth(consumer_key="",
                        consumer_secret="",
                        token="",
                        token_secret="")

    t = twitter.Twitter(auth=auth)
    msg = text
    #送信
    t.statuses.update(status=msg)
