from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    for member in message.new_chat_members:
        await message.reply_text(f"Welcome {member.mention} to **{message.chat.title}**! 🎉\n\nUse /help to see my powers.")

@Client.on_message(filters.command("setrules") & filters.group)
async def set_rules(client, message):
    # Logic to store rules would go here (Database)
    await message.reply_text("Group rules updated!")

@Client.on_message(filters.command("rules") & filters.group)
async def get_rules(client, message):
    await message.reply_text("📌 **Group Rules:**\n1. Be respectful.\n2. No spam.\n3. No links.")

@Client.on_message(filters.text & filters.group & ~filters.me)
async def anti_link(client, message):
    if "t.me/" in message.text or "http" in message.text:
        # Check if user is admin before deleting (simplified)
        try:
            await message.delete()
            await message.reply_text(f"🚫 {message.from_user.mention}, links are not allowed here!")
        except:
            pass
