from pyrogram import Client, filters
import time

@Client.on_message(filters.command("id"))
async def get_id(client, message):
    text = f"👤 **User ID:** `{message.from_user.id}`\n"
    text += f"💬 **Chat ID:** `{message.chat.id}`"
    await message.reply_text(text)

@Client.on_message(filters.command("ping"))
async def ping(client, message):
    start_time = time.time()
    msg = await message.reply_text("Pinging... 🏓")
    end_time = time.time()
    speed = round((end_time - start_time) * 1000, 2)
    await msg.edit(f"Pong! 🏓\nSpeed: `{speed}ms`")

@Client.on_message(filters.command("info"))
async def user_info(client, message):
    user = message.from_user
    if message.reply_to_message:
        user = message.reply_to_message.from_user

    text = f"✨ **User Info** ✨\n\n"
    text += f"First Name: {user.first_name}\n"
    text += f"Last Name: {user.last_name or 'N/A'}\n"
    text += f"Username: @{user.username or 'N/A'}\n"
    text += f"ID: `{user.id}`\n"
    await message.reply_text(text)
