import re
import random

from telegram import Update, ChatMember
from telegram.ext import MessageHandler, ContextTypes, filters

from settings import STATIC_DIR
from utils.logger import STDOUT_LOGGER as logger


VENT_PATTERN = ".*([дД][уУ][шШ][нН][иИоО][тТлЛ]).*"
MENTION_PATTERN = r'@(\w+)'


async def vent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    if re.match(VENT_PATTERN, user_message) is not None:
        vent_number = random.randint(1, 4)
        user_names = re.findall(MENTION_PATTERN, user_message)

        for chat_member in user_names:
            await context.bot.send_message(update.effective_chat.id, f'@{chat_member} не душни')

        await context.bot.send_photo(update.effective_chat.id, photo=open(f'{STATIC_DIR}/vent_{vent_number}.jpg', 'rb'))

VENT_HANDLER = MessageHandler(filters.TEXT, vent)
