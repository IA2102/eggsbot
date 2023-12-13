import time
from collections import defaultdict, deque

from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters

from utils.logger import STDOUT_LOGGER as logger

user_dict = defaultdict(lambda: deque(maxlen=15))


async def find_flood(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.forward_date is None:
        return

    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    username = update.effective_user.username
    current_time = time.time()
    logger.info("user_id = %d, username = %s", user_id, username)

    if len(user_dict[username]) >= 12 and user_dict[username][0] >= current_time - 15:
        user_dict[username].clear()
        await context.bot.send_message(
            chat_id=chat_id,
            text=f'@{username}, ты наказан за флуд. Подумай над своим поведением! (10 сек)'
        )
        await context.bot.ban_chat_member(chat_id, user_id)
        time.sleep(10)
        await context.bot.unban_chat_member(chat_id, user_id)
        telegram_link = await context.bot.create_chat_invite_link(
            chat_id, time.time() + 3600, name="Ты прощён. Возвращайся!"
        )
        await context.bot.send_message(user_id, telegram_link.invite_link)
    else:
        while user_dict[username]:
            if user_dict[username][0] <= current_time - 15:
                user_dict[username].popleft()
            else:
                break
        user_dict[username].append(time.time())


FIND_FLOOD_HANDLER = MessageHandler(filters.CHAT, find_flood)
