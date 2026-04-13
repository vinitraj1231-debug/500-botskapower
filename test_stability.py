import asyncio
import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

async def test_all_components():
    print("--- Comprehensive Bot Test ---")

    # 1. Check Directories
    dirs = ["plugins", "database", "utils", "downloads"]
    for d in dirs:
        if os.path.exists(d):
            print(f"✅ Directory {d} exists.")
        else:
            print(f"❌ Directory {d} MISSING.")

    # 2. Check Database
    from database.db import get_clones, add_clone, remove_clone
    await add_clone("test_stable_token", 999)
    clones = await get_clones()
    if any(c["bot_token"] == "test_stable_token" for c in clones):
        print("✅ DB: Add/Get clone works.")
    await remove_clone("test_stable_token")

    # 3. Check Plugins
    plugin_files = os.listdir("plugins")
    required_plugins = ["start.py", "clone.py", "music.py", "admin.py", "tools.py", "fun.py"]
    for p in required_plugins:
        if p in plugin_files:
            print(f"✅ Plugin {p} found.")
        else:
            print(f"❌ Plugin {p} MISSING.")

    # 4. Check Config
    from config import API_ID, BOT_TOKEN
    if API_ID and BOT_TOKEN:
        print("✅ Config: API_ID and BOT_TOKEN are set.")
    else:
        print("❌ Config: Missing credentials.")

    print("--- Test Complete ---")

if __name__ == "__main__":
    asyncio.run(test_all_components())
