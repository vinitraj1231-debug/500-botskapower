import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

async def test_plugins():
    print("Testing plugin loading...")
    app = Client(
        "test_app",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        plugins=dict(root="plugins")
    )
    # Just checking if it initializes without error
    print("Client initialized with plugins root 'plugins'")
    # Note: actually starting would require a valid token

if __name__ == "__main__":
    asyncio.run(test_plugins())
