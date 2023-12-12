from telegram import Update
from telegram.ext import ContextTypes, filters, CommandHandler


async def slap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    source = update.effective_user.username
    dest = context.args[0]
    message = f'@{source} шлёпнул {dest} по лицу селёдкой'

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


SLAP_HANDLER = CommandHandler("slap", slap, filters.COMMAND, has_args=True)
