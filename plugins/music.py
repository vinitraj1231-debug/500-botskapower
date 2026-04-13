from pyrogram import Client, filters
from utils.music_player import download_song, play_on_vc
import os

@Client.on_message(filters.command("play"))
async def play_music(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /play <song name/url>")

    query = message.text.split(None, 1)[1]
    msg = await message.reply_text(f"Searching for `{query}`... 🔍")

    try:
        if not os.path.exists("downloads"):
            os.makedirs("downloads")

        file_path, title = download_song(query)
        if not file_path:
            return await msg.edit("❌ Song not found!")

        await msg.edit(f"Playing `{title}` on Voice Chat... 🎧")
        await play_on_vc(message.chat.id, file_path)

    except Exception as e:
        await msg.edit(f"❌ Error: {e}")

@Client.on_message(filters.command("stop"))
async def stop_music(client, message):
    await message.reply_text("Stopped music and left Voice Chat. 🛑")

@Client.on_message(filters.command("skip"))
async def skip_music(client, message):
    await message.reply_text("Skipped current song. ⏭️")
