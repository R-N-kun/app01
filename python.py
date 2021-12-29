# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler

def start(bot, update):
  update.message.reply_text("I'm a bot, Nice to meet you!")

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater()
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  dispatcher.add_handler(start_handler)

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()
