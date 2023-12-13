import datetime
import random

import pytz
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, filters, ContextTypes

from db.db import birthdays, chat_id, birthday_wishes
from utils.logger import STDOUT_LOGGER as logger


async def happy_birthday(context: CallbackContext):
    today = datetime.date.today()
    day = today.strftime('%d')
    month = today.strftime('%m')
    today_string = day + '-' + month
    user_id = birthdays.get(today_string)
    logger.info("Enter")
    if user_id is not None:
        logger.info("Enter")
        await context.bot.send_message(
            chat_id=chat_id,
            text='@' + user_id + ', с днём рождения! ' + birthday_wishes[random.randint(0, len(birthday_wishes) - 1)]
        )


async def check_birthday(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    job = context.chat_data.get('polling_job')

    if job:
        await context.bot.send_message(chat_id=update.effective_chat.id, text='A polling job is already running!')
    else:
        job = context.job_queue.run_daily(
            happy_birthday,
            time=datetime.time(hour=0, minute=0, tzinfo=pytz.timezone('Europe/Chisinau'))
        )
        context.chat_data['polling_job'] = job
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Happy birthday is activated')


BIRTHDAY_HANDLER = CommandHandler('checkbirthday', check_birthday, filters.COMMAND)

