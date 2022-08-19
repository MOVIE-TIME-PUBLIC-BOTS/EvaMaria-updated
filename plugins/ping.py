"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters


# RANDOM
ALIVE = "I AM ALWAYS ALIVE BRO⚡️ITS MINNAL TIME⚡️💥"
GROUP = "<b>MOVIE TIME GROUP</b> ›› https://t.me/Movietym_official_group"
# -- Constants End -- #


@Client.on_message(filters.command("alive"))
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("group"))
async def group(_, message):
    await message.reply_text(GROUP)
    
#JUST TRIED A NEW FEATURE - ATHOLOKAM
