from telegram.ext import ApplicationBuilder

import settings
from handlers import *

app = ApplicationBuilder().token(settings.TELEGRAM_TOKEN).build()

app.add_handler(EGGS_HANDLER)
app.add_handler(FIND_FLOOD_HANDLER, group=1)
app.add_handler(CALL_ALL_HANDLER, group=2)
app.add_handler(VENT_HANDLER, group=3)
app.add_handler(SLAP_HANDLER, group=4)
app.add_handler(BIRTHDAY_HANDLER, group=5)

app.run_polling()
