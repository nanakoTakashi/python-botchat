#imports
import telebot
from datatime import datatime
#main puplic var's
now = datetime.now()


#TOKEN
TOKEN = '5353696413:AAG5PDs7YKW0FhW8HP6c0pUU6MJf4meyyoo'
app = telebot.TeleBot(TOKEN)
print("{now}: TOKEN is running")


#puplic var's
uid = message.from_user.id

#mithods
@app.message_handler(commands=["start"])
def starting(message):
  mci = message.chat.id
  app.send_message(mci, "hello!")
  


#polling

app.polling()
