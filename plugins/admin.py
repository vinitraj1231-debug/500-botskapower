from pyrogram import Client, filters
from pyrogram.types import ChatPermissions

@Client.on_message(filters.command("ban") & filters.group)
async def ban_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to ban them.")

    user_id = message.reply_to_message.from_user.id
    await client.ban_chat_member(message.chat.id, user_id)
    await message.reply_text(f"Banned {message.reply_to_message.from_user.first_name}! 🚫")

@Client.on_message(filters.command("kick") & filters.group)
async def kick_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to kick them.")

    user_id = message.reply_to_message.from_user.id
    await client.ban_chat_member(message.chat.id, user_id)
    await client.unban_chat_member(message.chat.id, user_id)
    await message.reply_text(f"Kicked {message.reply_to_message.from_user.first_name}! 👢")

@Client.on_message(filters.command("mute") & filters.group)
async def mute_user(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to mute them.")

    user_id = message.reply_to_message.from_user.id
    await client.restrict_chat_member(message.chat.id, user_id, ChatPermissions())
    await message.reply_text(f"Muted {message.reply_to_message.from_user.first_name}! 🔇")
