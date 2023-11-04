from telegram.ext import ApplicationBuilder

from handlers import *

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handlers([
    EGGS_HANDLER,
    CALL_ALL_HANDLER
])

app.run_polling()
