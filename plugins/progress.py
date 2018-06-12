from slackbot.bot import listen_to

@listen_to('進捗ありません')
def progress(message):
	message.send('ドンマイ') 

