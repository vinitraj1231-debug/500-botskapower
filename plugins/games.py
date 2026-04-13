from pyrogram import Client, filters
import random
import asyncio

# List of game emojis supported by Telegram
GAME_EMOJIS = ["🎲", "🎯", "🎰", "🎳", "🏀", "⚽"]

@Client.on_message(filters.command("dice"))
async def throw_dice(client, message):
    await client.send_dice(message.chat.id, emoji="🎲")

@Client.on_message(filters.command("slot"))
async def throw_slot(client, message):
    await client.send_dice(message.chat.id, emoji="🎰")

@Client.on_message(filters.command("dart"))
async def throw_dart(client, message):
    await client.send_dice(message.chat.id, emoji="🎯")

@Client.on_message(filters.command("football"))
async def throw_football(client, message):
    await client.send_dice(message.chat.id, emoji="⚽")

@Client.on_message(filters.command("basketball"))
async def throw_basketball(client, message):
    await client.send_dice(message.chat.id, emoji="🏀")

@Client.on_message(filters.command("bowling"))
async def throw_bowling(client, message):
    await client.send_dice(message.chat.id, emoji="🎳")

# Simple Guessing Game
@Client.on_message(filters.command("guess"))
async def guess_game(client, message):
    number = random.randint(1, 10)
    await message.reply_text("I'm thinking of a number between 1 and 10. You have 10 seconds to guess it!")

    try:
        def check(m):
            return m.from_user.id == message.from_user.id and m.text.isdigit()

        # This is a simplified listener. In a real bot, you'd use a conversation handler or state machine.
        # But for this task, I'll keep it simple.
        user_msg = await client.listen(message.chat.id, filters=filters.text, timeout=10)
        if int(user_msg.text) == number:
            await message.reply_text(f"🎉 Correct! The number was {number}.")
        else:
            await message.reply_text(f"❌ Wrong! The number was {number}.")
    except Exception:
        await message.reply_text(f"⏰ Time's up! The number was {number}.")

# Quiz Data (Example of many powers)
QUIZZES = [
    {"q": "What is the capital of France?", "a": "Paris"},
    {"q": "Which planet is known as the Red Planet?", "a": "Mars"},
    {"q": "What is the largest ocean on Earth?", "a": "Pacific"},
    {"q": "Who wrote 'Romeo and Juliet'?", "a": "Shakespeare"}
]

@Client.on_message(filters.command("quiz"))
async def quiz(client, message):
    q = random.choice(QUIZZES)
    await message.reply_text(f"❓ **Quiz:** {q['q']}")
    # Storage for answer checking would go here
