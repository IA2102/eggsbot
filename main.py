from telegram.ext import ApplicationBuilder

import settings
from handlers import *

app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

app.add_handler([
    EGGS_HANDLER,
])
app.add_handler(VENT_HANDLER, group=1)

app.run_polling()
