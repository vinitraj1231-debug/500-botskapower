from pyrogram import Client, filters
from database.db import add_clone, get_clones, remove_clone
from config import API_ID, API_HASH

@Client.on_message(filters.command("clone"))
async def clone_bot(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /clone <bot_token>")

    bot_token = message.text.split(None, 1)[1]
    msg = await message.reply_text("Cloning your bot... ⏳")

    try:
        # Verify token by trying to start a temporary client
        temp_client = Client(
            name=f"temp_{bot_token[:10]}",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=bot_token
        )
        await temp_client.start()
        bot_info = await temp_client.get_me()
        await temp_client.stop()

        # Add to DB
        await add_clone(bot_token, message.from_user.id)

        await msg.edit(f"✅ Bot Cloned Successfully!\n\n**Bot Name:** {bot_info.first_name}\n**Bot Username:** @{bot_info.username}")

        # Start the clone in the background (simplified for this task)
        # In a real scenario, you'd manage this more robustly
        new_clone = Client(
            name=f"clone_{bot_token[:10]}",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=bot_token,
            plugins=dict(root="plugins")
        )
        await new_clone.start()

    except Exception as e:
        await msg.edit(f"❌ Failed to clone bot.\n\n**Error:** {e}")

@Client.on_message(filters.command("cloned"))
async def list_clones(client, message):
    clones = await get_clones()
    user_clones = [c for c in clones if c["user_id"] == message.from_user.id]

    if not user_clones:
        return await message.reply_text("You haven't cloned any bots yet.")

    text = "🤖 **Your Cloned Bots:**\n\n"
    for i, clone in enumerate(user_clones, 1):
        text += f"{i}. `{clone['bot_token'][:15]}...`\n"

    await message.reply_text(text)
