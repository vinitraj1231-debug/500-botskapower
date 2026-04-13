from pyrogram import Client, filters

# ⚠️ Yahan apna NEW token dalna (old wala use mat karna)
BOT_TOKEN = "8691837145:AAHVgKQVHl9DAdWTYun-cuoDm1G0kaHBKPs"
API_ID = 8756786934        # my.telegram.org se lo
API_HASH = "your_api_hash"

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Start command
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name} 👋\n\n"
        "Main tumhara advanced Telegram bot hoon 🚀"
    )

# Help command
@app.on_message(filters.command("help"))
async def help_cmd(client, message):
    await message.reply_text(
        "/start - Bot start\n"
        "/help - Help menu\n"
        "/id - Tumhari ID"
    )

# User ID check
@app.on_message(filters.command("id"))
async def get_id(client, message):
    await message.reply_text(
        f"👤 Your ID: {message.from_user.id}"
    )

# Echo system (jo likhega wahi reply)
@app.on_message(filters.text & ~filters.command(["start", "help", "id"]))
async def echo(client, message):
    await message.reply_text(f"Echo: {message.text}")

app.run()
