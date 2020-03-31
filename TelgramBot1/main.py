from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from config import TG_TOKEN
from config import TG_API_URL
REQUEST_KWARGS={
    'proxy_url': 'socks4://171.103.9.22:4145/',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'assert_hostname': 'False',
        'cert_reqs': 'CERT_NONE'
        # 'username': 'user',
        # 'password': 'password'
    }
}
def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Hi!",
    )

def do_echo(bot: Bot, update: Update):
    text = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )
def main():
    bot = Bot (
        token = TG_TOKEN,
        request_kwargs=REQUEST_KWARGS
    )
    updater = Updater (
        bot =bot,
    )
    start_handler = CommandHandler('start', do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()