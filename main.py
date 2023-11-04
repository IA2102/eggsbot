from telegram.ext import ApplicationBuilder

from handlers.eggs import CALL_ALL_HANDLER
from settings import TELEGRAM_TOKEN
from handlers import *

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handlers([
    EGGS_HANDLER,
    CALL_ALL_HANDLER
])

app.run_polling()
