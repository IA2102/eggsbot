from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, filters

user_ids = ('DanilaY13', 'vitalicaraivanov', 'Diacon_Anastasia', 'toadski', 'npowell931', 'tdktxjrxhrx', 'bigboug',
            'ericad02', 'BA_RS_01', 'memejunky', 'beautifulmorning', 'eriomenco_nik')


async def call_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mention_all = " ".join([f"@{user_id}" for user_id in user_ids])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=mention_all)


CALL_ALL_HANDLER = CommandHandler("callall", call_all, filters.COMMAND)
