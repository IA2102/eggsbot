import re

from telegram import Update
from telegram.ext import ContextTypes, filters, MessageHandler

from db.db import user_ids

ALL_PATTERN = ".*(@all).*"


async def call_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    if re.match(ALL_PATTERN, user_message) is not None:
        mention_all = " ".join([f"@{user_id}" for user_id in user_ids])
        await context.bot.send_message(chat_id=update.effective_chat.id, text=mention_all)

CALL_ALL_HANDLER = MessageHandler(filters.TEXT, call_all)
