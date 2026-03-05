import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.environ.get("TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

def start(update, context):
    context.bot.send_message(chat_id=CHANNEL_ID, text="Bot sudah jalan!")

updater = Updater(TOKEN, use_context=True)
updater.dispatcher.add_handler(CommandHandler("start", start))

updater.start_polling()
updater.idle()
