#imports
import telebot
from datatime import datatime
# log file
start_time= datetime.now()
file = open('log.txt', 'a')

#TOKEN
TOKEN = "#Type your token here... "
app = telebot.TeleBot(TOKEN)
file.write(f"\n {datetime.now()} :- TOKEN is running")
print(f"{datetime.now()}: TOKEN is running")


#mithods
@app.message_handler(commands=["start"])
def starting(message):
  mci = message.chat.id
  uid = message.from_user.id
  app.send_message(mci, "hello!")
  file.write("{datetime.now()} :- /start:::: //{uid}// Hello! \n")
  


#polling
file.write("{datetime.now()} :- POLLING")
file.close
app.polling()
