from telegram.ext import ApplicationBuilder

from handlers import *

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(EGGS_HANDLER)
app.add_handler(FIND_FLOOD_HANDLER, group=1)
app.add_handler(CALL_ALL_HANDLER, group=2)

app.run_polling()
