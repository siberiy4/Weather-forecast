import sendtweet
from maketext import weather
import urllib.request
import urllib.error
import json
import testtext
from wwebhook import to_slack
import slackweb
import twitter




text = testtext.weather('270000')
sendtweet.tweettext(text)
to_slack(text+'\n <!channel>')


