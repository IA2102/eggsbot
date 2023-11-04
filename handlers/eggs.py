import glob
import re
import random
import time
from collections import defaultdict, deque

from utils.logger import STDOUT_LOGGER as logger
from settings import STATIC_DIR
from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters, CommandHandler

EGGS_PATTERN = ".*([яЯ][иИЙй][ЧчЦц]).*"
user_ids = ('DanilaY13', 'vitalicaraivanov', 'Diacon_Anastasia', 'toadski', 'npowell931', 'tdktxjrxhrx', 'bigboug',
            'ericad02', 'BA_RS_01', 'memejunky', 'beautifulmorning', 'eriomenco_nik')
user_dict = defaultdict(lambda: deque(maxlen=11))


async def eggs(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    logger.info("[%s] %s", update.message.chat.username, user_message)
    if re.match(EGGS_PATTERN, user_message) is not None:
        file_list = glob.glob(STATIC_DIR + '/*')
        is_moshonka = random.randint(1, 100) <= 5
        egg_number = 0 if is_moshonka else random.randint(1, len(file_list) - 2)

        await context.bot.send_photo(update.effective_chat.id, photo=open(f'{STATIC_DIR}/eggs_{egg_number}.jpg', 'rb'))


# async def find_flood(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     logger.info("Заходим в find_flood")
#     user_id = update.effective_user.id
#     username = update.effective_user.username
#     current_time = time.time()
#
#     if len(user_dict[username]) >= 0 and len(user_dict[username]) >= 9 and user_dict[username][0] >= current_time - 20:
#         user_dict[username].clear()
#         await context.bot.send_message(
#             chat_id=update.effective_chat.id,
#             text=f'@{username}, ты наказан за флуд. Подумай над своим поведением! (10 сек)'
#         )
#         await context.bot.restrict_chat_member(
#             update.effective_chat.id,
#             user_id,
#             telegram.ChatPermissions(can_send_messages=False)
#         )
#         time.sleep(10)
#         await context.bot.restrict_chat_member(
#             update.effective_chat.id,
#             user_id,
#             telegram.ChatPermissions(can_send_messages=True)
#         )
#     else:
#         while user_dict[username]:
#             if user_dict[username][0] <= current_time - 20:
#                 user_dict[username].popleft()
#             else:
#                 break
#         user_dict[username].append(time.time())

async def find_flood(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    username = update.effective_user.username
    current_time = time.time()
    logger.info("user_id = %d, username = %s", user_id, username)

    if len(user_dict[username]) >= 0 and len(user_dict[username]) >= 9 and user_dict[username][0] >= current_time - 20:
        user_dict[username].clear()
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f'@{username}, ты наказан за флуд. Подумай над своим поведением! (10 сек)'
        )
        await context.bot.ban_chat_member(update.effective_chat.id, user_id)
        time.sleep(10)
        await context.bot.unban_chat_member(update.effective_chat.id, user_id)
    else:
        while user_dict[username]:
            if user_dict[username][0] <= current_time - 20:
                user_dict[username].popleft()
            else:
                break
        user_dict[username].append(time.time())


async def call_all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mention_all = " ".join([f"@{user_id}" for user_id in user_ids])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=mention_all)


EGGS_HANDLER = MessageHandler(filters.TEXT, eggs)
FIND_FLOOD_HANDLER = MessageHandler(filters.TEXT, find_flood)
CALL_ALL_HANDLER = CommandHandler("callall", call_all, filters.COMMAND)


