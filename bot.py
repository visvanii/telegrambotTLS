# imports n shiz
import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

#Variables
updater = Updater(token='1094957116:AAEn2Xy_LK9bmvlylHZPKX_Cz9QNBD8AVqQ', use_context=True)
dispatcher = updater.dispatcher

#functions
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="h e l p o")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def setDate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="temp")

def horo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="hold on")

#main
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)

date_handler = CommandHandler('setDate', setDate)
dispatcher.add_handler(date_handler)

horo_handler = CommandHandler('horoscope', horo)
dispatcher.add_handler(horo_handler)


updater.start_polling()
print ('bot be working bitch')