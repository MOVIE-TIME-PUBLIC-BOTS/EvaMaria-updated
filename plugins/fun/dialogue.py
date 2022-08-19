from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random


#SOME RANDOM DIALOGUES


@Client.on_message(filters.private & filters.command("dialogues"))
async def dialogues(bot, message):
    await message.reply_text(
        text=random.choice(DIALOGUES)
    )   


DIALOGUES = [
  "Powerful people come from powerful places",
  "If you gain courage because a thousand people are standing behind you, then you can only win a war. But if a thousand people get courage because you are standing in front of them, you can conquer the world",
  "The one who comes with a gang is a gangster. He always comes alone. Monster !!!",
  "Mother is the greatest warrior of the world !!!",
  "Angane Pavanayi Shavamayi. Enthokke Bahalamarunnu, Malappuram kathi, machine gun, bomb, olakkede moodu",
  "Pani varunund Avaracha"
]
