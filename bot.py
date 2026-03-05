import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime, timedelta

# Ambil token dari Railway Variables
TOKEN = os.getenv("TOKEN")

# Simpan data member (sementara pakai dictionary)
members = {}

# Logging biar gampang debug
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Command /renew -> otomatis 30 hari
def renew(update: Update, context: CallbackContext):
    try:
        username = context.args[0]
        days = 30  # default masa aktif 30 hari
        expire_date = datetime.now() + timedelta(days=days)
        members[username] = expire_date
        update.message.reply_text(f"{username} diperpanjang {days} hari.\nExpired: {expire_date.strftime('%d-%m-%Y %H:%M')}")
    except Exception as e:
        update.message.reply_text("Format salah. Contoh: /renew @username")

# Command /check -> cek masa aktif
def check(update: Update, context: CallbackContext):
    try:
        username = context.args[0]
        if username in members:
            expire_date = members[username]
            update.message.reply_text(f"{username} aktif sampai {expire_date.strftime('%d-%m-%Y %H:%M')}")
        else:
            update.message.reply_text(f"{username} belum terdaftar.")
    except Exception as e:
        update.message.reply_text("Format salah. Contoh: /check @username")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("renew", renew))
    dp.add_handler(CommandHandler("check", check))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
