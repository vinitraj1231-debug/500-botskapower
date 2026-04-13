import json
import os
import asyncio

DB_FILE = "database/clones.json"
lock = asyncio.Lock()

def ensure_db():
    if not os.path.exists(DB_FILE):
        os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
        with open(DB_FILE, "w") as f:
            json.dump([], f)

async def add_clone(bot_token, user_id):
    async with lock:
        ensure_db()
        with open(DB_FILE, "r") as f:
            clones = json.load(f)

        for clone in clones:
            if clone["bot_token"] == bot_token:
                clone["user_id"] = user_id
                break
        else:
            clones.append({"bot_token": bot_token, "user_id": user_id})

        with open(DB_FILE, "w") as f:
            json.dump(clones, f)

async def get_clones():
    async with lock:
        ensure_db()
        with open(DB_FILE, "r") as f:
            return json.load(f)

async def remove_clone(bot_token):
    async with lock:
        ensure_db()
        with open(DB_FILE, "r") as f:
            clones = json.load(f)

        clones = [c for c in clones if c["bot_token"] != bot_token]

        with open(DB_FILE, "w") as f:
            json.dump(clones, f)
