from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters

from db.db import user_ids


async def call_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mention_all = " ".join([f"@{user_id}" for user_id in user_ids])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=mention_all)


CALL_ALL_HANDLER = CommandHandler("callall", call_all, filters.COMMAND)
