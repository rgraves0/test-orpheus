import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = 'YOUR_TOKEN'

def start(update, context):
    update.message.reply_text('Hello! I am your music archiving bot. Use /archive <link> to archive a music link.')

def archive(update, context):
    if context.args:
        link = context.args[0]
        # Here you would call the OrpheusDL archiving function
        # For example: os.system(f'python3 orpheus.py {link}')
        update.message.reply_text(f'Archiving {link}...')
    else:
        update.message.reply_text('Please provide a link to archive.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("archive", archive))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
