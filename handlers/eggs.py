import re
import random
from utils.logger import STDOUT_LOGGER as logger
from settings import STATIC_DIR
from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters

EGGS_PATTERN = ".*([яЯ][иИЙй][ЧчЦц]).*"


async def eggs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    logger.info("[%s] %s", update.message.chat.username, user_message)
    if re.match(EGGS_PATTERN, user_message) is not None:
        egg_number = random.randint(1, 4)
        await context.bot.send_photo(update.effective_chat.id, photo=open(f'{STATIC_DIR}/eggs_{egg_number}.jpg', 'rb'))

EGGS_HANDLER = MessageHandler(filters.TEXT, eggs)
