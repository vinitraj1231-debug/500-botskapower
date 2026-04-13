import json
import os
import asyncio
import aiofiles

DB_FILE = "database/clones.json"
lock = asyncio.Lock()

async def ensure_db():
    if not os.path.exists(DB_FILE):
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        async with aiofiles.open(DB_FILE, "w") as f:
            await f.write(json.dumps([]))

async def add_clone(bot_token, user_id):
    async with lock:
        await ensure_db()
        async with aiofiles.open(DB_FILE, "r") as f:
            content = await f.read()
            clones = json.loads(content)

        for clone in clones:
            if clone["bot_token"] == bot_token:
                clone["user_id"] = user_id
                break
        else:
            clones.append({"bot_token": bot_token, "user_id": user_id})

        async with aiofiles.open(DB_FILE, "w") as f:
            await f.write(json.dumps(clones))

async def get_clones():
    async with lock:
        await ensure_db()
        async with aiofiles.open(DB_FILE, "r") as f:
            content = await f.read()
            return json.loads(content)

async def remove_clone(bot_token):
    async with lock:
        await ensure_db()
        async with aiofiles.open(DB_FILE, "r") as f:
            content = await f.read()
            clones = json.loads(content)

        clones = [c for c in clones if c["bot_token"] != bot_token]

        async with aiofiles.open(DB_FILE, "w") as f:
            await f.write(json.dumps(clones))
