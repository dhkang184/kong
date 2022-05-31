import telegram
#token : 5201362764:AAGG4CnWmRLws0Sy1ofXAuiTLpd1A6mJsF8

chat_token = '5201362764:AAGG4CnWmRLwsOSy1ofXAuiTLpd1A6mJsF8'
#chat_token = "HTTP API"
bot_id = '1978950146'

# chat = telegram.Bot(token = chat_token)
# updates = chat.getUpdates()
# for u in updates:
#     print(u.message['chat']['id'])


bot = telegram.Bot(token = chat_token)
text = '안녕하세요'
bot.sendMessage(chat_id = bot_id, text=text)