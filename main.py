from telegram.ext import ApplicationBuilder
from settings import TELEGRAM_TOKEN
from handlers import *

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handlers([
    EGGS_HANDLER,
])

app.run_polling()
