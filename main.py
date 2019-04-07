from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
from datetime import date, datetime

# INFO:
# emojis: https://apps.timwhitlock.info/emoji/tables/unicode

'''''''''''''''''
CONSTANTS 
'''''''''''''''''
CHAT_ID = 
TOKEN_ID = 

'''''''''''''''''
REMINDER LIST
'''''''''''''''''
class Reminder(object):
    def __init__(self, days, message):
        self.days = days
        self.message = message

my_reminders = [
    Reminder([7, 14], 'Remember be happy')
]

'''''''''''''''''
BOT LOGIC
'''''''''''''''''
# Send Dog Photos: https://medium.freecodecamp.org/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(TOKEN_ID)
    dp = updater.dispatcher

    today = date.today();
    '''''''''''''''''
    Remiders send message:
    '''''''''''''''''
    for reminder in my_reminders:
        if today.day in reminder.days:
            dp.bot.send_message(chat_id=CHAT_ID, text=reminder.message)
            print datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ': Send Message: ' + reminder.message

    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()