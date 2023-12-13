import glob
import re

from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters

from settings import VENT_DIR

VENT_PATTERN = ".*([дД][уУ][шШ][нН][иИоО]).*"
MENTION_PATTERN = r'@(\w+)'

counter = 1


async def vent(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    if re.match(VENT_PATTERN, user_message) is not None:
        file_list = glob.glob(VENT_DIR + '/*')
        global counter
        counter = counter + 1 if counter < len(file_list) else 1
        vent_number = counter
        user_names = re.findall(MENTION_PATTERN, user_message)

        for chat_member in user_names:
            await context.bot.send_message(update.effective_chat.id, f'@{chat_member} не душни')

        await context.bot.send_photo(update.effective_chat.id, photo=open(f'{VENT_DIR}/vent_{vent_number}.jpg', 'rb'))


VENT_HANDLER = MessageHandler(filters.TEXT, vent)
