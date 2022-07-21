from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import Constants as keys
from telegram import *
import Responses as R


print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type something to get started (press /help for help)')


def help_command(update, context):
    update.message.reply_text('you can enter greetings')
    update.message.reply_text('you can enter "average: grade1 credit1 grade2 credit2 ... to get your average')
    update.message.reply_text('enter week day')
    update.message.reply_text('type search: and the content you wont to get results on the internet')
    update.message.reply_text('type wiki: and a first and last name of famous individual to get his birth date'
                              '(must have capslock at start of first and last name) ')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f'Update {update} caused error {context.error}')


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
