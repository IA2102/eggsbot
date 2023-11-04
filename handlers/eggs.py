import glob
import re
import random
from utils.logger import STDOUT_LOGGER as logger
from settings import STATIC_DIR
from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters, CommandHandler

EGGS_PATTERN = ".*([яЯ][иИЙй][ЧчЦц]).*"


async def eggs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    logger.info("[%s] %s", update.message.chat.username, user_message)
    if re.match(EGGS_PATTERN, user_message) is not None:
        file_list = glob.glob(STATIC_DIR + '/*')
        is_moshonka = random.randint(1, 100) <= 5
        egg_number = 0 if is_moshonka else random.randint(1, len(file_list) - 2)

        await context.bot.send_photo(update.effective_chat.id, photo=open(f'{STATIC_DIR}/eggs_{egg_number}.jpg', 'rb'))


async def call_all(update: Update, context):
    chat_id = update.message.chat_id
    members = context.bot.get_chat_members(chat_id)

    mention_all = " ".join([f"@{member.user.username}" for member in members if member.user.username])
    await context.bot.send_message(chat_id, f"{mention_all}")


EGGS_HANDLER = MessageHandler(filters.TEXT, eggs)
CALL_ALL_HANDLER = CommandHandler('callAll', call_all)


