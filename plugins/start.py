from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name} 👋\n\n"
        "Main tumhara highly advanced multi-functional bot hoon! 🚀\n\n"
        "Use /help to see what I can do."
    )

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text(
        "🤖 **Bot Commands:**\n\n"
        "• /clone <token> - Apna clone bot banayein\n"
        "• /play <song> - Music play karein (VC)\n"
        "• /id - Tumhari ID\n"
        "• /ping - Bot speed check karein"
    )
