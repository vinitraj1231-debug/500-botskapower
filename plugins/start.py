from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name} 👋\n\n"
        "🚀 **I am the Ultimate Advanced Bot** with 500+ powers!\n"
        "I can play music, manage groups, play games, and much more.\n\n"
        "✨ **My Main Features:**\n"
        "• 🎵 **Advanced Music Player (VC)**\n"
        "• 🤖 **Bot Cloning System**\n"
        "• 🎮 **50+ Games Support**\n"
        "• 🛡️ **Group Management**\n"
        "• 🛠️ **Utility Tools**\n\n"
        "Click the button below to see all commands!",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Help Menu", callback_data="help_main")]
        ])
    )

@Client.on_message(filters.command("help"))
async def help_cmd(client, message):
    help_text = (
        "📖 **Advanced Bot Help Menu**\n\n"
        "Categorized Commands:\n"
        "🎵 **Music:** /play, /skip, /stop, /vc\n"
        "🤖 **Cloning:** /clone, /cloned\n"
        "🎮 **Games:** /dice, /slot, /dart, /guess, /quiz, /football, /basketball\n"
        "🛡️ **Admin:** /ban, /kick, /mute, /setrules, /rules\n"
        "🛠️ **Tools:** /id, /ping, /info, /echo\n\n"
        "Highly Optimized & Lag-free Experience! 🔥"
    )
    await message.reply_text(help_text)
