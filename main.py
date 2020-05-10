#!/usr/bin/env python3.8
"""This is a prototype software
"""

__author__ = "Nikita Miropolskiy"
__email__ = "m@ker.su"
__license__ = "no license, proprietary code"
__status__ = "Prototype"
__title__ = "quentin"
__version__ = "0.1"
__url__ = "https://github.com/nikat/quentin"
__description__ = \
    """This is quentin bot.
    """

import logging
import yaml
from aiogram import Bot, Dispatcher, executor, types

LOG_LEVEL = logging.DEBUG

CONFIG = yaml.load(open('config.yml'), Loader=yaml.BaseLoader)

BUILT_FROM = CONFIG['general']['built-from']

TELEGRAM_TOKEN = CONFIG['telegram']['token']
TELEGRAM_PROXY = CONFIG['telegram']['proxy']
CHATS = CONFIG['telegram']['chats']

logging.basicConfig(level=LOG_LEVEL)
bot = Bot(token=TELEGRAM_TOKEN, proxy=TELEGRAM_PROXY)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'], chat_id=CHATS)
async def send_welcome(message: types.Message):
    logging.log(logging.WARNING, 'chat=%s' % message.chat.id)
    await message.reply(__description__, disable_web_page_preview=True)


@dp.message_handler(commands=['version'], chat_id=CHATS)
async def send_version(message: types.Message):
    commit = '\n  from {commit}'.format(commit=BUILT_FROM) if BUILT_FROM != 'NONE' else ''
    reply_text = '<a href="{url}">{title}</a> v{version}\n  by {author}&lt;{email}&gt;{commit}'.format(
        title=__title__, version=__version__, author=__author__,
        email=__email__, commit=commit, url=__url__
    )
    await message.reply(reply_text, reply=False, parse_mode='HTML', disable_web_page_preview=True)


@dp.message_handler(chat_id=CHATS)
async def echo(message: types.Message):
    logging.log(logging.DEBUG, 'chat=%s' % message.chat.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
