 from telegram.ext import Updater, CommandHandler
 import requests
 import re
 def getUrl():
 #obtain a json object with image details
 #extract image url from the json object
 contents = requests.get('https://api.thecatapi.com/v1/images/search')
 url = contents[0]['url']
 return url
 def sendImage(bot, update):
 url = getUrl()
 chat_id = update.message.chat_id
 bot.send_photo(chat_id=chat_id, image=url)
 def main():
 updater = Updater("5029994413:AAFlqFJDWGLWPs30_lZFkmC7EJt5M4wWyk8")
 #call sendImage() when the user types a command in the telegram chat
 updater.dispatcher.add_handler(CommandHandler('meow',sendImage))
 #start the bot
 updater.start_polling()
 updater.idle()
 if __name__ == '__main__':
 main()
