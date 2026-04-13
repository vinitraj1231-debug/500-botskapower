import asyncio
from database.db import add_clone, get_clones, remove_clone

async def test():
    print("Testing DB...")
    try:
        await add_clone("test_token", 12345)
        print("Add clone success")
        clones = await get_clones()
        print(f"Get clones: {clones}")
        await remove_clone("test_token")
        print("Remove clone success")
        print("DB Test Passed (assuming Mongo is reachable or it will timeout)")
    except Exception as e:
        print(f"DB Test Failed: {e}")

if __name__ == "__main__":
    asyncio.run(test())
