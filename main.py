import os
import asyncio
import aiofiles
from pyrogram import Client, filters
from pyromod import listen
from config import API_ID, API_HASH, BOT_TOKEN
from database.db import get_clones

class AdvancedBot(Client):
    def __init__(self):
        super().__init__(
            "AdvancedBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="plugins")
        )

    async def start(self):
        await super().start()
        print("Main Bot Started! 🚀")

        # Start clones
        clones = await get_clones()
        for clone_data in clones:
            try:
                token = clone_data["bot_token"]
                client = Client(
                    name=f"clone_{token[:10]}",
                    api_id=API_ID,
                    api_hash=API_HASH,
                    bot_token=token,
                    plugins=dict(root="plugins")
                )
                await client.start()
                print(f"Clone started for token: {token[:10]}...")
            except Exception as e:
                print(f"Failed to start clone: {e}")

    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped!")

if __name__ == "__main__":
    app = AdvancedBot()
    app.run()
