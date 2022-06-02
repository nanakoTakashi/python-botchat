#imports
import telebot
from datatime import datatime
#main puplic var's
now = datetime.now()
file = open('log.txt', 'a')

#TOKEN
TOKEN = '5353696413:AAG5PDs7YKW0FhW8HP6c0pUU6MJf4meyyoo'
app = telebot.TeleBot(TOKEN)
file.write("\n {datetime.now()} :- TOKEN is running")
print("{now}: TOKEN is running")


#puplic var's
uid = message.from_user.id

#mithods
@app.message_handler(commands=["start"])
def starting(message):
  mci = message.chat.id
  uid = message.from_user.id
  app.send_message(mci, "hello!")
  file.write("{now} :- /start:::: //{uid}// Hello! \n")
  


#polling
file.write("{datetime.now()} :- POLLING")
file.close
app.polling()
