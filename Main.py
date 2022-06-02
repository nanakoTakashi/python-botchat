#imports
import telebot
from datatime import datatime

now = datetime.now()

#TOKEN
TOKEN = '5353696413:AAG5PDs7YKW0FhW8HP6c0pUU6MJf4meyyoo'
app = telebot.TeleBot(TOKEN)
print("{now}: TOKEN is running")


#puplic var's


#polling

app.polling()
