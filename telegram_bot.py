from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your OrpheusDL bot.')

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
