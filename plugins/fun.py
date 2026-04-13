from pyrogram import Client, filters
import random

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "I'm on a seafood diet. I see food and I eat it."
]

@Client.on_message(filters.command("joke"))
async def send_joke(client, message):
    await message.reply_text(random.choice(JOKES))

@Client.on_message(filters.command("echo"))
async def echo(client, message):
    if len(message.command) < 2:
        return
    await message.reply_text(message.text.split(None, 1)[1])
